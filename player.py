import pygame


class Player:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.dx = 5
        self.img = pygame.image.load(img)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.dx

        if keys[pygame.K_RIGHT]:
            self.x += self.dx

        if keys[pygame.K_SPACE]:
            pass

        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736

        self.update()

    def update(self):
        return self.img, (self.x, self.y)




