import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Invasión espacial")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

in_exec = True
while in_exec:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_exec = False
    
    # Gray Space background
    screen.fill((100, 100, 100))
    pygame.display.update()

pygame.quit()