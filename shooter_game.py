import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)

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


class Bullet:
    def __init__(self, x, y):
        super().__init__
        self.image = pygame.Surface([4,15])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

        self.speed = 10

    def update(self):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill() 



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
    
    
    keys = pygame.key.get_pressed()
    player.move(keys)
      
    SCREEN.fill(BLACK) 

    player.draw(SCREEN)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()