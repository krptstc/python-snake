import pygame
import random
import time
pygame.init()

from constants import *
from colors import *

WINDOW_SIZE = (GAME_WIDTH, GAME_HEIGHT)
SCREEN      = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

snake_head = [2, 1]
snake      = [snake_head, [1, 1], [0, 1]]
h_vel      = 1
v_vel      = 0

clock = pygame.time.Clock()

def check_if_alive(snake):
    if snake[0][0] < 0 or snake[0][0] > GAME_WIDTH / TILE_SIZE - 1:
        return False
    elif snake[0][1] < 0 or snake[0][1] > GAME_HEIGHT / TILE_SIZE - 1:
        return False
    else:
        return True

def generate_food(snake):
    food_x = random.randint(0, GAME_WIDTH / TILE_SIZE - 1)
    food_y = random.randint(0, GAME_HEIGHT / TILE_SIZE - 1)
    while [food_x, food_y] in snake:
        food_x = random.randint(0, GAME_WIDTH / TILE_SIZE - 1)
        food_y = random.randint(0, GAME_HEIGHT / TILE_SIZE - 1)
    return [food_x, food_y]

current_food = generate_food(snake)

def grow_snake(snake):
    snake.append(snake[-1])

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

    if len(snake) < 2:
        snake_head[0] += h_vel
        snake_head[1] += v_vel
    else:
        del snake[-1]
        snake.insert(1, [snake_head[0], snake_head[1]])
        snake_head[0] += h_vel
        snake_head[1] += v_vel

    running = check_if_alive(snake)

    if snake_head == current_food:
        current_food = generate_food(snake)
        grow_snake(snake)
        pygame.mixer.music.load('eat_food.wav')
        pygame.mixer.music.play(0)

    for tile in snake:
        pygame.draw.rect(SCREEN, COLOR_PRIMARY, pygame.Rect(tile[0] * TILE_SIZE, tile[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(SCREEN, COLOR_SECONDARY, pygame.Rect(current_food[0] * TILE_SIZE, current_food[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.update()
    clock.tick(1 / WAIT_TIME)

pygame.mixer.music.load('death.wav')
pygame.mixer.music.play(0)
time.sleep(1)
