import pygame


class GameConfig:
    pygame.init()
    WINDOW_W = 800
    WINDOW_H = 800
    health = 3
    score = 0
    meilleurScore = 0
    bonus_init = -1
    count = 0
    playerBullets = []
    asteroids = []
    stars = []
    aliens = []
    alienBullets = []
    window = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    clock = pygame.time.Clock()

    background = pygame.image.load('images/Background.png')
    ennemi = pygame.image.load('images/Ennemi.png')
    playerRocket = pygame.image.load('images/Spaceship.png')
    bonus = pygame.image.load('images/Bonus.png')
    meteorite_petite = pygame.image.load('images/Meteorite_Petite.png')
    meteorite_moyenne = pygame.image.load('images/Meteorite_Moyenne.png')
    meteorite_grande = pygame.image.load('images/Meteorite_Grande.png')

    def init():
        GameConfig.background = pygame.image.load('images/Background.png')
        GameConfig.ennemi = pygame.image.load('images/Ennemi.png')
        GameConfig.playerRocket = pygame.image.load('images/Spaceship.png')
        GameConfig.bonus = pygame.image.load('images/Bonus.png')
        GameConfig.meteorite_petite = pygame.image.load('images/Meteorite_Petite.png')
        GameConfig.meteorite_moyenne = pygame.image.load('images/Meteorite_Moyenne.png')
        GameConfig.meteorite_grande = pygame.image.load('images/Meteorite_Grande.png')