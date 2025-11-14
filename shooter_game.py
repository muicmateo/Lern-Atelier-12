import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space-Invaders")

clock = pygame.time.Clock()
FPS = 60


class Player:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
    
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


# Liste für alle Schüsse
bullets = []

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
        # Schuss abfeuern bei Leertaste
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = player.shoot()
                bullets.append(bullet)
    
    # Tastatureingaben für Bewegung
    keys = pygame.key.get_pressed()
    player.move(keys)
    
    # Aktualisiere alle Schüsse
    for bullet in bullets:
        bullet.update()
    
    # Entferne Schüsse, die den Bildschirm verlassen haben
    bullets = [bullet for bullet in bullets if not bullet.is_off_screen()]
      
    SCREEN.fill(BLACK) 

    # Zeichne Spieler
    player.draw(SCREEN)
    
    # Zeichne alle Schüsse
    for bullet in bullets:
        bullet.draw(SCREEN)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()