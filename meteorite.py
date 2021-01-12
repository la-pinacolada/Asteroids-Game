import random
from game_config import *


class Meteorite(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = GameConfig.meteorite_petite
        elif self.rank == 2:
            self.image = GameConfig.meteorite_moyenne
        else:
            self.image = GameConfig.meteorite_grande
        self.w = 50 * rank
        self.h = 50 * rank
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
        self.xv = self.xdir * random.randrange(1, 3)
        self.yv = self.ydir * random.randrange(1, 3)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))