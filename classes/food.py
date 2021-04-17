import pygame
import random

from modules.constants import *

class Food:
    def __init__(self):
        self.x = 0
        self.y = 0

    def new_position(self, snake_body):
        self.x = random.randint(0, GAME_WIDTH / TILE_SIZE - 1)
        self.y = random.randint(0, GAME_HEIGHT / TILE_SIZE - 1)

        while [self.x, self.y] in snake_body:
            self.new_position(snake_body)

        return [self.x, self.y]

    def check_for_collision(self, snake):
        if [self.x, self.y] in snake.body:
            self.new_position(snake.body)
            snake.grow()
            pygame.mixer.music.load('sound/eat_food.wav')
            pygame.mixer.music.play(0)
