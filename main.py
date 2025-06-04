import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

in_exec = True
while in_exec:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_exec = False