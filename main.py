import pygame
pygame.init()

WINDOW_SIZE = (800, 600)
SCREEN      = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill((255, 0, 0))
    pygame.display.update()
