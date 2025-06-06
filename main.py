import pygame
from classes import Player, Enemy, Bullet
import sys
from pygame import mixer
import random

frame_rate = 60


def restart_game(screen, player):
    player.score = 0
    player.is_alive = True
    player.level = 1
    player.x = screen.get_width() / 2 - 32
    player.y = screen.get_height() - 64
    player.x_change = 0
    player.y_change = 0
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
    bullets = []
    return (enemies, bullets)


def startup():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    background = pygame.image.load("background2.jpg")
    pygame.display.set_caption("Invasión espacial")
    icon = pygame.image.load("alien.png")
    pygame.display.set_icon(icon)
    mixer.music.load("MusicaFondo.mp3")
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)

    # Player position. He starts in the middle of the screen, in the bottom.
    player = Player(
        screen,
        screen.get_width() / 2 - 32,
        screen.get_height() - 64,
        pygame.image.load("spaceship.png"),
    )  # 64x64

    enemies, _ = restart_game(screen, player)
    try:
        main_loop(screen, background, player, enemies)
    except Exception:
        print("Error: ", sys.exc_info())


def main_loop(screen, background, player, enemies):
    level = 1
    in_exec = True
    clock = pygame.time.Clock()
    bullets = []
    while in_exec:
        # Gray Space background
        screen.blit(background, (0, 0))
        draw_score(screen, player)
        draw_level(screen, level)
        game_over = player_movement(player, bullets, enemies)
        if game_over and player.is_alive:
            in_exec = False
        elif game_over and not player.is_alive:
            level = 1
            enemies, bullets = restart_game(screen, player)
        add_enemies = 0
        for enemy in enemies:
            if not enemy.is_alive:
                add_enemies += 1
                player.score += 10 * enemy.level
        if add_enemies > 0:
            level += 1
            enemies.extend(
                [
                    Enemy(
                        screen,
                        random.randint(0, int(screen.get_width()) - 16),
                        random.randint(0, int(screen.get_height() / 2 - 16)),
                        pygame.image.load("alien.png"),
                        level,
                    )
                ]
                * add_enemies
            )
        enemies = [enemy for enemy in enemies if enemy.is_alive]
        for enemy in enemies:
            enemy.update_position()
            enemy.draw()
        pygame.display.update()
        clock.tick(frame_rate)
    pygame.quit()


def draw_score(screen, player):
    font = pygame.font.Font("Fastest.ttf", 30)
    score_text = font.render(f"Puntaje: {player.score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


def draw_level(screen, level):
    font = pygame.font.Font("Fastest.ttf", 26)
    level_text = font.render(f"Nivel: {level}", True, (255, 255, 255))
    screen.blit(level_text, (10, 50))


def game_over(screen, player):
    font = pygame.font.Font("Fastest.ttf", 20)
    game_over_text = font.render(
        f"Perdiste, tu puntaje fue de {player.score} puntos",
        True,
        (255, 255, 255),
    )
    screen.blit(
        game_over_text,
        (
            screen.get_width() / 2 - game_over_text.get_width() / 2,
            screen.get_height() / 2 - game_over_text.get_height() / 2,
        ),
    )


def player_movement(player, bullets, enemies):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player.is_alive:
                player.move_x(-1)
            if event.key == pygame.K_RIGHT and player.is_alive:
                player.move_x(1)
            if event.key == pygame.K_UP and player.is_alive:
                player.move_y(-1)
            if event.key == pygame.K_DOWN and player.is_alive:
                player.move_y(1)
            if event.key == pygame.K_SPACE and player.is_alive:
                mixer.Sound("disparo.mp3").play()
                bulletIcon = pygame.image.load("bullet.png")
                # Rotate the bullet icon 90 degrees clockwise
                bulletIcon = pygame.transform.rotate(bulletIcon, -90)
                bullets.append(
                    Bullet(
                        player.screen,
                        player.x + player.image.get_width() / 2 - 8,
                        player.y,
                        bulletIcon,
                    )
                )
            if event.key == pygame.K_ESCAPE:
                return True
        if event.type == pygame.KEYUP:
            if (
                event.key == pygame.K_LEFT
                or event.key == pygame.K_RIGHT
                and player.is_alive
            ):
                player.move_x(0)
            if (
                event.key == pygame.K_UP
                or event.key == pygame.K_DOWN
                and player.is_alive
            ):
                player.move_y(0)
    if player.is_alive:
        for enemy in enemies:
            bullet = enemy.shoot(player)
            if bullet:
                bullets.append(bullet)
        player.update_position()
        player.draw()
    else:
        game_over(player.screen, player)
    # Remove bullets that are out of the screen
    bullets = [
        bullet
        for bullet in bullets
        if (5 <= bullet.y <= 595) and (5 <= bullet.x <= 795) and bullet.is_alive
    ]
    for bullet in bullets:
        bullet.update_position()
        bullet.draw()
    check_collisions(bullets, enemies, player)
    return False


def object_collision(object1, object2):
    return pygame.Rect.colliderect(object1.rect, object2.rect)


def check_collisions(bullets, enemies, player):
    for bullet in bullets:
        if bullet.destination_x != 0 and bullet.destination_y != 0:
            if object_collision(bullet, player) and player.is_alive:
                mixer.Sound("dead.mp3").play()
                player.is_alive = False
                bullet.is_alive = False
        for enemy in enemies:
            if (
                bullet.destination_x == 0
                and bullet.destination_y == 0
                and object_collision(bullet, enemy)
            ):
                mixer.Sound("Golpe.mp3").play()
                bullet.is_alive = False
                enemy.is_alive = False
    for enemy in enemies:
        if object_collision(player, enemy) and player.is_alive:
            mixer.Sound("dead.mp3").play()
            player.is_alive = False


# Start the game
startup()
