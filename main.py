import pygame
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

    for tile in snake:
        pygame.draw.rect(SCREEN, COLOR_PRIMARY, pygame.Rect(tile[0] * TILE_SIZE, tile[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.update()
    clock.tick(1 / WAIT_TIME)
