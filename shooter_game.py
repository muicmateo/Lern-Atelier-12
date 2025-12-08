import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space-Invaders")

clock = pygame.time.Clock()
FPS = 60

# Font für HUD
font = pygame.font.Font(None, 36)


class Player:
    def __init__(self, x, y, width, height, speed, color, lives=3):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.lives = lives
    
    def move(self, keys):
        """Horizontale Bewegung mit Begrenzung im Fenster"""
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        
        # Begrenzung der Bewegung im Fenster
        if self.x < 0:
            self.x = 0
        if self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width
    
    def draw(self, screen):
        """Zeichnet den Spieler auf dem Bildschirm"""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def shoot(self):
        """Erstellt einen neuen Schuss in der Mitte des Spielers"""
        bullet_x = self.x + self.width // 2 - 2
        bullet_y = self.y
        return Bullet(bullet_x, bullet_y)


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 4
        self.height = 15
        self.speed = 10
        self.color = YELLOW

    def update(self):
        """Bewegung des Schusses nach oben"""
        self.y -= self.speed

    def draw(self, screen):
        """Zeichnet den Schuss auf dem Bildschirm"""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def is_off_screen(self):
        """Prüft, ob der Schuss den Bildschirm verlassen hat"""
        return self.y + self.height < 0
    
    def get_rect(self):
        """Gibt das Rechteck des Schusses für Kollisionserkennung zurück"""
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Alien:
    """Ein einfacher Alien mit horizontaler Bewegung"""
    def __init__(self, x, y, width=40, height=30, color=GREEN, speed=2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.direction = 1  

    def update(self):
        """Bewegt den Alien horizontal"""
        self.x += self.speed * self.direction

    def draw(self, screen):
        """Zeichnet den Alien auf dem Bildschirm"""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def check_edges(self):
        """Gibt True zurück, wenn der Alien eine Bildschirmkante erreicht hat"""
        return self.x + self.width >= SCREEN_WIDTH or self.x <= 0

    def drop_down(self, pixels=20):
        """Lässt den Alien absinken und kehrt die Richtung um"""
        self.y += pixels
        self.direction *= -1
    
    def get_rect(self):
        """Gibt das Rechteck des Aliens für Kollisionserkennung zurück"""
        return pygame.Rect(self.x, self.y, self.width, self.height)


def create_alien_fleet(rows, cols, start_x, start_y, h_spacing, v_spacing):
    """Erzeugt eine Liste mit einer Matrix von Aliens"""
    aliens = []
    for r in range(rows):
        for c in range(cols):
            x = start_x + c * h_spacing
            y = start_y + r * v_spacing
            aliens.append(Alien(x, y))
    return aliens


class HUD:
    """Head-Up Display für Punktzahl und Leben"""
    def __init__(self, font, color=WHITE):
        self.font = font
        self.color = color
    
    def draw_score(self, screen, score, x=10, y=10):
        """Zeigt die aktuelle Punktzahl an"""
        score_text = self.font.render(f"Score: {score}", True, self.color)
        screen.blit(score_text, (x, y))
    
    def draw_lives(self, screen, lives, x=650, y=10):
        """Zeigt die verbleibenden Leben an"""
        lives_text = self.font.render(f"Lives: {lives}", True, self.color)
        screen.blit(lives_text, (x, y))
    
    def draw(self, screen, score, lives):
        """Zeichnet das komplette HUD am oberen Bildschirmrand"""
        self.draw_score(screen, score)
        self.draw_lives(screen, lives)


# Liste für alle Schüsse
bullets = []

# Erstelle Alien-Fleet (3 Reihen, 8 Spalten)
aliens = create_alien_fleet(rows=3, cols=8, start_x=50, start_y=50, h_spacing=80, v_spacing=60)

# Punktesystem
score = 0

# HUD initialisieren
hud = HUD(font)

player_width = 50
player_height = 40
player_speed = 5
player_x = (SCREEN_WIDTH / 2) - (player_width / 2)
player_y = SCREEN_HEIGHT - player_height - 10

player = Player(player_x, player_y, player_width, player_height, player_speed, RED)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = player.shoot()
                bullets.append(bullet)
    
    
    keys = pygame.key.get_pressed()
    player.move(keys)
    
   
    for bullet in bullets:
        bullet.update()
    
    
    bullets = [bullet for bullet in bullets if not bullet.is_off_screen()]
    
    
    edge_hit = False
    for alien in aliens:
        alien.update()
        if alien.check_edges():
            edge_hit = True
    
   
    if edge_hit:
        for alien in aliens:
            alien.drop_down()
    
  
    
    # Kollisionserkennung zwischen Bullets und Aliens
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.get_rect().colliderect(alien.get_rect()):
                # Alien entfernen
                aliens.remove(alien)
                # Schuss entfernen
                bullets.remove(bullet)
                # Punkte erhöhen
                score += 10
                break
      
    SCREEN.fill(BLACK) 

   
    player.draw(SCREEN)
    
    
    for bullet in bullets:
        bullet.draw(SCREEN)

    
    for alien in aliens:
        alien.draw(SCREEN)
    
    # HUD anzeigen (Punkte und Leben)
    hud.draw(SCREEN, score, player.lives)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()