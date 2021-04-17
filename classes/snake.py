import pygame

from modules.constants import *
from modules.colors import *

class Snake:
    def __init__(self):
        self.head  = [2, 1]
        self.body  = [self.head, [1, 1], [0, 1]]
        self.h_vel = 1
        self.v_vel = 0

    def draw(self):
        for tile in self.body:
            pygame.draw.rect(SCREEN, COLOR_PRIMARY, pygame.Rect(tile[0] * TILE_SIZE, tile[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def move(self):
        self.head[0] += self.h_vel
        self.head[1] += self.v_vel

    def check_if_alive(self):
        if self.head[0] < 0 or self.head[0] > GAME_WIDTH / TILE_SIZE - 1:
            return False
        elif self.head[1] < 0 or self.head[1] > GAME_HEIGHT / TILE_SIZE - 1:
            return False

        no_head = self.body.copy()
        del no_head[0]

        if self.head in no_head:
            return False
        return True

    def grow(self):
        self.body.append(self.body[-1])
