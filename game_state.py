import random
from player import *


class GameState:
    def __init__(self):
        GameConfig.player = Player()
        GameConfig.playerBullets = []
        GameConfig.asteroids = []
        GameConfig.count = 0
        GameConfig.stars = []
        GameConfig.aliens = []
        GameConfig.alienBullets = []

    def advance_state(self):
        GameConfig.window.blit(GameConfig.background, (0, 0))

        GameConfig.player.draw(GameConfig.window)
        for a in GameConfig.asteroids:
            a.draw(GameConfig.window)
        for b in GameConfig.playerBullets:
            b.draw(GameConfig.window)
        for s in GameConfig.stars:
            s.draw(GameConfig.window)
        for a in GameConfig.aliens:
            a.draw(GameConfig.window)
        for b in GameConfig.alienBullets:
            b.draw(GameConfig.window)