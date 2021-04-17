import pygame
pygame.init()

WINDOW_SIZE = (800, 600)
SCREEN      = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

from constants import *
from colors import *

snake_head = [1, 1]
snake      = (snake_head)
h_vel      = 1
v_vel      = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            h_vel = 1
            v_vel = 0
        elif keys[pygame.K_LEFT]:
            h_vel = -1
            v_vel = 0
        elif keys[pygame.K_UP]:
            h_vel = 0
            v_vel = -1
        elif keys[pygame.K_DOWN]:
            h_vel = 0
            v_vel = 1

    SCREEN.fill(COLOR_DARK)

    if len(snake) - 1 == 1:
        snake_head[0] += h_vel
        snake_head[1] += v_vel

    print(snake)

    pygame.draw.rect(SCREEN, COLOR_PRIMARY, pygame.Rect(snake_head[0] * TILE_SIZE, snake_head[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.update()
    clock.tick(1 / WAIT_TIME)
