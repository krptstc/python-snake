import pygame
import time
pygame.init()

from classes.snake import Snake
from classes.food import Food

from modules.constants import *
from modules.colors import *

pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake = Snake()
current_food = Food()
current_food.new_position(snake.body)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            snake.h_vel = 1
            snake.v_vel = 0
        elif keys[pygame.K_LEFT]:
            snake.h_vel = -1
            snake.v_vel = 0
        elif keys[pygame.K_UP]:
            snake.h_vel = 0
            snake.v_vel = -1
        elif keys[pygame.K_DOWN]:
            snake.h_vel = 0
            snake.v_vel = 1

    SCREEN.fill(COLOR_DARK)

    if len(snake.body) < 2:
        snake.move()
        snake.head[0] += h_vel
        snake.head[1] += v_vel
    else:
        del snake.body[-1]
        snake.body.insert(1, [snake.head[0], snake.head[1]])
        snake.move()

    running = snake.check_if_alive()
    current_food.check_for_collision(snake)

    snake.draw()
    pygame.draw.rect(SCREEN, COLOR_SECONDARY, pygame.Rect(current_food.x * TILE_SIZE, current_food.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.update()
    clock.tick(1 / WAIT_TIME)

pygame.mixer.music.load('sound/death.wav')
pygame.mixer.music.play(0)
time.sleep(1)
