import random
from pygame import Rect
import pygame
from math import sqrt, atan2, degrees
import time


class Entity:
    def __init__(self, screen, x, y, image, border_size=10):
        self.is_alive = True
        self.screen = screen
        self.x = int(x)
        self.y = int(y)
        self.image = image
        self.x_change = 0
        self.y_change = 0
        self.x_change_speed = 2
        self.y_change_speed = 2
        self.border_size = border_size
        self.rect = Rect(
            self.x, self.y, self.image.get_width(), self.image.get_height()
        )

    def check_frontier_x_left(self):
        if self.x <= self.border_size:
            return False
        return True

    def check_frontier_x_right(self):
        if (
            self.x
            >= self.screen.get_width() - self.image.get_width() - self.border_size
        ):
            return False
        return True

    def check_frontier_y_up(self):
        if self.y <= self.border_size:
            return False
        return True

    def check_frontier_y_down(self):
        if (
            self.y
            >= self.screen.get_height() - self.image.get_height() - self.border_size
        ):
            return False
        return True

    def draw(self):
        self.screen.blit(self.image, (int(self.x), int(self.y)))

    def move_x(self, direction=0):
        self.x_change = self.x_change_speed * direction

    def move_y(self, direction=0):
        self.y_change = self.y_change_speed * direction

    def update_position(self):
        if (not self.check_frontier_x_left() and self.x_change < 0) or (
            not self.check_frontier_x_right() and self.x_change > 0
        ):
            self.x_change = 0
        if (not self.check_frontier_y_up() and self.y_change < 0) or (
            not self.check_frontier_y_down() and self.y_change > 0
        ):
            self.y_change = 0

        self.x = int(self.x + self.x_change)
        self.y = int(self.y + self.y_change)
        self.rect = Rect(
            self.x, self.y, self.image.get_width(), self.image.get_height()
        )


class Player(Entity):
    def __init__(self, screen, x, y, image):
        super().__init__(screen, x, y, image, 5)
        self.x_change_speed = 4
        self.y_change_speed = 4
        self.score = 0


class Enemy(Entity):
    def __init__(self, screen, x, y, image, level=1):
        super().__init__(screen, x, y, image, 2)
        self.shoot_cooldown = int(60000 / level)
        self.last_shot = 0
        self.can_shoot = level > 10
        self.level = level
        self.x_change_speed = int(5 * level)
        self.y_change_speed = int(5 * level)
        self.x_change = 2
        self.y_change = 2

    def update_position(self):
        if random.randint(0, 100) < 5:
            self.x_change = random.randint(-3, 3)
            self.y_change = random.randint(-3, 3)
        super().update_position()

    def shoot(self, player):
        if self.can_shoot:
            now = int(time.time() * 1000)
            if now - self.last_shot > self.shoot_cooldown:
                # Set epoch time to shoot in millis
                self.last_shot = now
                bullet_icon = pygame.image.load("bullet_enemy.png")
                # Rotate the bullet icon to face the player
                angle = atan2(player.y - self.y, player.x - self.x)
                # Convert to degrees
                angle = degrees(angle)
                bullet_icon = pygame.transform.rotate(bullet_icon, angle)
                bullet = Bullet(
                    self.screen,
                    self.x,
                    self.y,
                    bullet_icon,
                    player.x,
                    player.y,
                )
                bullet.x_change_speed = 2
                bullet.y_change_speed = 2
                return bullet
        return None


class Bullet(Entity):
    def __init__(self, screen, x, y, image, destination_x=0, destination_y=0):
        super().__init__(screen, x, y, image, 1)
        self.destination_x = destination_x
        self.destination_y = destination_y
        self.x_change_speed = 0
        self.y_change_speed = 7
        self.x_change = 0
        self.y_change = 0
        self.delta_x = destination_x - x
        self.delta_y = destination_y - y

    def update_position(self):
        if self.destination_x != 0 and self.destination_y != 0:
            # Move towards the destination using a vector from x,y to destination_x,destination_y
            newX, newY = self.new_position()
            self.x = newX
            self.y = newY
        else:
            self.y -= self.y_change_speed
        super().update_position()

    def new_position(self):
        distance = sqrt(self.delta_x**2 + self.delta_y**2)
        if distance == 0:
            self.is_alive = False
            return self.destination_x, self.destination_y
        u_x = self.delta_x / distance
        u_y = self.delta_y / distance
        return self.x + u_x * self.y_change_speed, self.y + u_y * self.y_change_speed
