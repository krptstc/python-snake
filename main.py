import pygame
import time
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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(COLOR_DARK)

    if len(snake) - 1 == 1:
        snake_head[0] += h_vel
        snake_head[1] += v_vel

    print(snake)

    pygame.draw.rect(SCREEN, COLOR_PRIMARY, pygame.Rect(snake_head[0] * TILE_SIZE, snake_head[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.update()
    pygame.time.wait(int(WAIT_TIME * 1000))
