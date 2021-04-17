import pygame
pygame.init()

WINDOW_SIZE = (800, 600)
SCREEN      = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

from constants import *
from colors import *

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(COLOR_DARK)
    pygame.draw.rect(SCREEN, COLOR_PRIMARY, pygame.Rect(40, 40, TILE_SIZE, TILE_SIZE))
    pygame.display.update()
