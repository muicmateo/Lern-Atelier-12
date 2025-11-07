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

player_width = 50
player_height = 40
player_speed = 5 

player_x = (SCREEN_WIDTH / 2) - (player_width / 2)
player_y = SCREEN_HEIGHT - player_height - 10

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
    SCREEN.fill(BLACK) 

    pygame.draw.rect(SCREEN, RED, (player_x, player_y, player_width, player_height))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()