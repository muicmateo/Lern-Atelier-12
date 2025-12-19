import pygame
import sys
import random

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

font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)


class Player:
    def __init__(self, x, y, width, height, speed, color, lives=3):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.lives = lives
        self.invincible = False
        self.invincible_timer = 0
    
    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        
        if self.x < 0:
            self.x = 0
        if self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width
    
    def draw(self, screen):
        if self.invincible and self.invincible_timer % 10 < 5:
            return
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def shoot(self):
        bullet_x = self.x + self.width // 2 - 2
        bullet_y = self.y
        return Bullet(bullet_x, bullet_y)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def take_damage(self):
        if not self.invincible:
            self.lives -= 1
            self.invincible = True
            self.invincible_timer = 120
    
    def update(self):
        if self.invincible:
            self.invincible_timer -= 1
            if self.invincible_timer <= 0:
                self.invincible = False


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 4
        self.height = 15
        self.speed = 10
        self.color = YELLOW

    def update(self):
        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def is_off_screen(self):
        return self.y + self.height < 0
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Alien:
    def __init__(self, x, y, width=40, height=30, color=GREEN, speed=2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.direction = 1

    def update(self):
        self.x += self.speed * self.direction

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def check_edges(self):
        return self.x + self.width >= SCREEN_WIDTH or self.x <= 0

    def drop_down(self, pixels=20):
        self.y += pixels
        self.direction *= -1
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class AlienBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 3
        self.height = 10
        self.speed = 5
        self.color = RED

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


def create_alien_fleet(rows, cols, start_x, start_y, h_spacing, v_spacing):
    aliens = []
    for r in range(rows):
        for c in range(cols):
            x = start_x + c * h_spacing
            y = start_y + r * v_spacing
            aliens.append(Alien(x, y))
    return aliens


class HUD:
    def __init__(self, font, color=WHITE):
        self.font = font
        self.color = color
    
    def draw_score(self, screen, score, x=10, y=10):
        score_text = self.font.render(f"Score: {score}", True, self.color)
        screen.blit(score_text, (x, y))
    
    def draw_lives(self, screen, lives, x=650, y=10):
        lives_text = self.font.render(f"Lives: {lives}", True, self.color)
        screen.blit(lives_text, (x, y))
    
    def draw(self, screen, score, lives):
        self.draw_score(screen, score)
        self.draw_lives(screen, lives)


def reset_game():
    bullets = []
    alien_bullets = []
    aliens = create_alien_fleet(rows=3, cols=8, start_x=50, start_y=50, h_spacing=80, v_spacing=60)
    score = 0
    alien_shoot_timer = 0
    
    player_width = 50
    player_height = 40
    player_speed = 5
    player_x = (SCREEN_WIDTH / 2) - (player_width / 2)
    player_y = SCREEN_HEIGHT - player_height - 10
    player = Player(player_x, player_y, player_width, player_height, player_speed, RED)
    
    return bullets, alien_bullets, aliens, score, alien_shoot_timer, player


def draw_game_over(screen, score):
    game_over_text = large_font.render("GAME OVER", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
    
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))


def draw_victory(screen, score):
    victory_text = large_font.render("VICTORY!", True, GREEN)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
    
    screen.blit(victory_text, (SCREEN_WIDTH // 2 - victory_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))


bullets, alien_bullets, aliens, score, alien_shoot_timer, player = reset_game()
alien_shoot_cooldown = 60
hud = HUD(font)
game_over = False
victory = False

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if game_over or victory:
                if event.key == pygame.K_r:
                    bullets, alien_bullets, aliens, score, alien_shoot_timer, player = reset_game()
                    game_over = False
                    victory = False
                elif event.key == pygame.K_q:
                    running = False
            else:
                if event.key == pygame.K_SPACE:
                    bullet = player.shoot()
                    bullets.append(bullet)
    
    if not game_over and not victory:
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.update()
        
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
        
        if len(aliens) > 0:
            alien_shoot_timer += 1
            if alien_shoot_timer >= alien_shoot_cooldown:
                shooting_alien = random.choice(aliens)
                bullet_x = shooting_alien.x + shooting_alien.width // 2 - 1
                bullet_y = shooting_alien.y + shooting_alien.height
                alien_bullets.append(AlienBullet(bullet_x, bullet_y))
                alien_shoot_timer = 0
        
        for alien_bullet in alien_bullets:
            alien_bullet.update()
        
        alien_bullets = [ab for ab in alien_bullets if not ab.is_off_screen()]

        for bullet in bullets[:]:
            for alien in aliens[:]:
                if bullet.get_rect().colliderect(alien.get_rect()):
                    aliens.remove(alien)
                    bullets.remove(bullet)
                    score += 10
                    break
        
        for alien_bullet in alien_bullets[:]:
            if alien_bullet.get_rect().colliderect(player.get_rect()):
                alien_bullets.remove(alien_bullet)
                player.take_damage()
        
        for alien in aliens:
            if alien.y + alien.height >= player.y:
                game_over = True
        
        if player.lives <= 0:
            game_over = True
        
        if len(aliens) == 0:
            victory = True
      
    SCREEN.fill(BLACK)
    
    if game_over:
        draw_game_over(SCREEN, score)
    elif victory:
        draw_victory(SCREEN, score)
    else:
        player.draw(SCREEN)
        
        for bullet in bullets:
            bullet.draw(SCREEN)

        for alien in aliens:
            alien.draw(SCREEN)
        
        for alien_bullet in alien_bullets:
            alien_bullet.draw(SCREEN)
        
        hud.draw(SCREEN, score, player.lives)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()