import math
from game_config import *


class Player(object):
    def __init__(self):
        self.img = GameConfig.playerRocket
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = GameConfig.WINDOW_W // 2
        self.y = GameConfig.WINDOW_H // 2
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosinus = math.cos(math.radians(self.angle + 90))
        self.sinus = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosinus * self.w // 2, self.y - self.sinus * self.h // 2)

    def draw(self, window):
        window.blit(self.rotatedSurf, self.rotatedRect)

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosinus = math.cos(math.radians(self.angle + 90))
        self.sinus = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosinus * self.w // 2, self.y - self.sinus * self.h // 2)

    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosinus = math.cos(math.radians(self.angle + 90))
        self.sinus = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosinus * self.w // 2, self.y - self.sinus * self.h // 2)

    def moveForward(self):
        self.x += self.cosinus * 6
        self.y -= self.sinus * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosinus = math.cos(math.radians(self.angle + 90))
        self.sinus = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosinus * self.w // 2, self.y - self.sinus * self.h // 2)

    def updateLocation(self):
        if self.x > GameConfig.WINDOW_W + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = GameConfig.WINDOW_W
        elif self.y < -50:
            self.y = GameConfig.WINDOW_W
        elif self.y > GameConfig.WINDOW_H + 50:
            self.y = 0