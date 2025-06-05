class Entity:
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.x_change = 0
        self.y_change = 0
        self.x_change_speed = 2
        self.y_change_speed = 2

    def check_frontier_x(self):
        print(self.x, self.screen.get_width(), self.image.get_width())
        if (
            self.x <= 10
            or self.x >= self.screen.get_width() - self.image.get_width() - 10
        ):
            return False
        return True

    def check_frontier_y(self):
        if (
            self.y <= 10
            or self.y >= self.screen.get_height() - self.image.get_height() - 10
        ):
            return False
        return True

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move_x(self, direction=0):
        print(self.x)
        if self.check_frontier_x():
            self.x += self.x_change_speed * direction

    def move_y(self, direction=0):
        if self.check_frontier_y():
            self.y += self.y_change_speed * direction


class Player(Entity):
    def __init__(self, screen, x, y, image):
        super().__init__(screen, x, y, image)
        self.x_change_speed = 4
        self.y_change_speed = 4
