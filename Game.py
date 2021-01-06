import pygame

pygame.init()

sw = 800
sh = 800


bg = pygame.image.load('images/starbg.png')
Playership =pygame.image.load('images/Playerspaceship.png')

pygame.display.set_caption('Asteroids')
win = pygame.display.set_mode((sw, sh))

clock = pygame.time.Clock()
gameover = False

class Player(object):
    def __init__(self):
        self.img = Playership
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw//2
        self.y = sh//2
        


def redrawGameWindow() :
    win.blit(bg, (0,0))

    pygame.display.update()


run = True
while run:
    clock.tick(60)
    if not gameover :
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()







pygame.quit()
