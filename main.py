import pygame
from classes import Player

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Invasión espacial")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# Player position. He starts in the middle of the screen, in the bottom.
player = Player(
    screen,
    screen.get_width() / 2,
    screen.get_height() - 64,
    pygame.image.load("spaceship.png"),
)  # 64x64


in_exec = True

frame_rate = 60
clock = pygame.time.Clock()

while in_exec:
    # Gray Space background
    screen.fill((100, 100, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_exec = False
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_LEFT:
                player.move_x(-1)
            if event.key == pygame.K_RIGHT:
                player.move_x(1)
            if event.key == pygame.K_UP:
                player.move_y(-1)
            if event.key == pygame.K_DOWN:
                player.move_y(1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.move_x(0)
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.move_y(0)
    player.draw()
    pygame.display.update()
    clock.tick(frame_rate)

pygame.quit()
