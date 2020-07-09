import pygame
from pygame import mixer

pygame.init()
playerImg = pygame.image.load('space.png')
mixer.music.load("background.wav")
mixer.music.set_volume(0.1)
mixer.music.play(-1)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.vel = 5

    def draw(self, win):
        win.blit(playerImg, (self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_SPACE]:
            bulletSound = mixer.Sound("laser.wav")
            bulletSound.set_volume(0.1)
            bulletSound.play()

        if self.x <= 0:
            self.x = 0
        elif self.x >= 836:
            self.x = 836
