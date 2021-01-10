import pygame


class GameConfig:
    pygame.init()
    pygame.display.set_caption("Arcade Asteroid")
    WINDOW_W = 800
    WINDOW_H = 800

    background = pygame.image.load('images/Background.png')
    ennemi = pygame.image.load('images/Ennemi.png')
    playerRocket = pygame.image.load('images/Spaceship.png')
    bonus = pygame.image.load('images/Bonus.png')
    meteorite_petite = pygame.image.load('images/Meteorite_Petite.png')
    meteorite_moyenne = pygame.image.load('images/Meteorite_Moyenne.png')
    meteorite_grande = pygame.image.load('images/Meteorite_Grande.png')

    Tir = pygame.mixer.Sound('sons/tir.mp3')
    Explosion_2 = pygame.mixer.Sound('sons/Explosion_Ennemi.wav')
    Explosion_1 = pygame.mixer.Sound('sons/Explosion.wav')
    Tir.set_volume(.25)
    Explosion_2.set_volume(.25)
    Explosion_1.set_volume(.25)

    window = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    clock = pygame.time.Clock()

