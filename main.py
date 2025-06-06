import pygame
from classes import Player, Enemy
import sys

frame_rate = 60


def startup():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    background = pygame.image.load("background2.jpg")
    pygame.display.set_caption("Invasión espacial")
    icon = pygame.image.load("alien.png")
    pygame.display.set_icon(icon)

    # Player position. He starts in the middle of the screen, in the bottom.
    player = Player(
        screen,
        screen.get_width() / 2 - 32,
        screen.get_height() - 64,
        pygame.image.load("spaceship.png"),
    )  # 64x64

    enemies = [
        Enemy(screen, 100 - 16, 50, pygame.image.load("alien.png")),
        Enemy(screen, 200 - 16, 50, pygame.image.load("alien.png")),
        Enemy(screen, 300 - 16, 50, pygame.image.load("alien.png")),
        Enemy(screen, 400 - 16, 50, pygame.image.load("alien.png")),
        Enemy(screen, 500 - 16, 50, pygame.image.load("alien.png")),
        Enemy(screen, 600 - 16, 50, pygame.image.load("alien.png")),
        Enemy(screen, 700 - 16, 50, pygame.image.load("alien.png")),
        Enemy(screen, 150 - 16, 100, pygame.image.load("alien.png")),
        Enemy(screen, 250 - 16, 100, pygame.image.load("alien.png")),
        Enemy(screen, 350 - 16, 100, pygame.image.load("alien.png")),
        Enemy(screen, 450 - 16, 100, pygame.image.load("alien.png")),
        Enemy(screen, 550 - 16, 100, pygame.image.load("alien.png")),
        Enemy(screen, 650 - 16, 100, pygame.image.load("alien.png")),
    ]
    try:
        main_loop(screen, background, player, enemies)
    except Exception:
        print("Error: ", sys.exc_info()[0])


def main_loop(screen, background, player, enemies):
    in_exec = True
    clock = pygame.time.Clock()
    while in_exec:
        # Gray Space background
        screen.blit(background, (0, 0))
        in_exec = player_movement(player)
        for enemy in enemies:
            enemy.update_position()
            enemy.draw()
        pygame.display.update()
        clock.tick(frame_rate)
    pygame.quit()


def player_movement(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
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
    player.update_position()
    player.draw()
    return True


# Start the game
startup()
