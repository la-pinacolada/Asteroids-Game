import random
from game_config import *


class Ennemi(object):
    def __init__(self):
        self.img = GameConfig.ennemi
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.ranPoint = random.choice(
            [(random.randrange(0, GameConfig.WINDOW_W - self.w), random.choice([-1 * self.h - 5, GameConfig.WINDOW_H + 5])),
             (random.choice([-1 * self.w - 5, GameConfig.WINDOW_W + 5]), random.randrange(0, GameConfig.WINDOW_H - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < GameConfig.WINDOW_W // 2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < GameConfig.WINDOW_H // 2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))