import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Invasión espacial")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# Player
player_icon = pygame.image.load("spaceship.png") # 64x64
# Player position. He starts in the middle of the screen, in the bottom.
player_x = 400 - 32
player_y = 550 - 32
player_x_change = 0

def player_draw(x, y):
    screen.blit(player_icon, (x, y))

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
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5

    player_x += player_x_change
    player_draw(player_x, player_y)
    pygame.display.update()
    clock.tick(frame_rate)

pygame.quit()