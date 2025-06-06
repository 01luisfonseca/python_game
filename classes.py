import random


class Entity:
    def __init__(self, screen, x, y, image, border_size=10):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.x_change = 0
        self.y_change = 0
        self.x_change_speed = 2
        self.y_change_speed = 2
        self.border_size = border_size

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
        self.screen.blit(self.image, (self.x, self.y))

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

        self.x += self.x_change
        self.y += self.y_change


class Player(Entity):
    def __init__(self, screen, x, y, image):
        super().__init__(screen, x, y, image, 5)
        self.x_change_speed = 4
        self.y_change_speed = 4


class Enemy(Entity):
    def __init__(self, screen, x, y, image):
        super().__init__(screen, x, y, image, 2)
        self.x_change_speed = 5
        self.y_change_speed = 5
        self.x_change = 1
        self.y_change = 1

    def update_position(self):
        if random.randint(0, 100) < 5:
            self.x_change = random.randint(-2, 2)
            self.y_change = random.randint(-2, 2)
        super().update_position()
