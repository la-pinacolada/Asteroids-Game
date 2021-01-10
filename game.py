import pygame
import math
import random
from game_config import *


gameover = False
health = 3
score = 0
meilleurScore = 0
bonus = False
bonus_init = -1
boolson = True


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
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def draw(self, window):
        window.blit(self.rotatedSurf, self.rotatedRect)

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def updateLocation(self):
        if self.x > GameConfig.WINDOW_W + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = GameConfig.WINDOW_W
        elif self.y < -50:
            self.y = GameConfig.WINDOW_W
        elif self.y > GameConfig.WINDOW_H + 50:
            self.y = 0


class Tir(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.s * 10

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), [self.x, self.y, self.w, self.h])

    def checkOffScreen(self):
        if self.x < -50 or self.x > GameConfig.WINDOW_W or self.y > GameConfig.WINDOW_H or self.y < -50:
            return True


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


class Bonus(object):
    def __init__(self):
        self.img = GameConfig.bonus
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


class TirEnnemi(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 4
        self.h = 4
        self.dx, self.dy = player.x - self.x, player.y - self.y
        self.dist = math.hypot(self.dx, self.dy)
        self.dx, self.dy = self.dx / self.dist, self.dy / self.dist
        self.xv = self.dx * 5
        self.yv = self.dy * 5

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), [self.x, self.y, self.w, self.h])


def game_loop():
    GameConfig.window.blit(GameConfig.background, (0, 0))
    font = pygame.font.SysFont('serif sans ms', 40)

    HealthText = font.render('Health : ' + str(health), 1, (204, 197, 185))
    ScoreText = font.render('Score Actuel : ' + str(score), 1, (204, 197, 185))
    MeilleurScoreText = font.render('Meilleur Score : ' + str(meilleurScore), 1, (204, 197, 185))
    TryAgainText = font.render('Game Over ( Press Tab to try again)', 1, (204, 197, 185))

    player.draw(GameConfig.window)
    for a in asteroids:
        a.draw(GameConfig.window)
    for b in playerBullets:
        b.draw(GameConfig.window)
    for s in stars:
        s.draw(GameConfig.window)
    for a in aliens:
        a.draw(GameConfig.window)
    for b in alienBullets:
        b.draw(GameConfig.window)

    if bonus:
        pygame.draw.rect(GameConfig.window, (0, 0, 0), [GameConfig.WINDOW_W // 2 - 51, 19, 102, 22])
        pygame.draw.rect(GameConfig.window, (255, 255, 255), [GameConfig.WINDOW_W // 2 - 50, 20, 100 - 100 * (count - bonus_init) / 500, 20])

    if gameover:
        GameConfig.window.blit(TryAgainText,
                 (GameConfig.WINDOW_W // 2 - TryAgainText.get_width() // 2, GameConfig.WINDOW_H // 2 - TryAgainText.get_height() // 2))
    GameConfig.window.blit(HealthText, (25, 25))
    GameConfig.window.blit(ScoreText, (25, 35 + HealthText.get_height()))
    GameConfig.window.blit(MeilleurScoreText, (25, 45 + HealthText.get_height() + ScoreText.get_height()))
    pygame.display.update()


player = Player()
playerBullets = []
asteroids = []
count = 0
stars = []
aliens = []
alienBullets = []
run = True
while run:
    GameConfig.clock.tick(60)
    count += 1
    if not gameover:
        if count % 50 == 0:
            ran = random.choice([1, 1, 1, 2, 2, 3])
            asteroids.append(Meteorite(ran))
        if count % 1000 == 0:
            stars.append(Bonus())
        if count % 750 == 0:
            aliens.append(Ennemi())
        for i, a in enumerate(aliens):
            a.x += a.xv
            a.y += a.yv
            if a.x > GameConfig.WINDOW_W + 150 or a.x + a.w < -100 or a.y > GameConfig.WINDOW_H + 150 or a.y + a.h < -100:
                aliens.pop(i)
            if count % 60 == 0:
                alienBullets.append(TirEnnemi(a.x + a.w // 2, a.y + a.h // 2))

            for b in playerBullets:
                if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                    if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                        aliens.pop(i)
                        if boolson:
                            GameConfig.Explosion_2.play()
                        score += 50
                        break

        for i, b in enumerate(alienBullets):
            b.x += b.xv
            b.y += b.yv
            if (
                    b.x >= player.x - player.w // 2 and b.x <= player.x + player.w // 2) or b.x + b.w >= player.x - player.w // 2 and b.x + b.w <= player.x + player.w // 2:
                if (
                        b.y >= player.y - player.h // 2 and b.y <= player.y + player.h // 2) or b.y + b.h >= player.y - player.h // 2 and b.y + b.h <= player.y + player.h // 2:
                    health -= 1
                    alienBullets.pop(i)
                    break

        player.updateLocation()
        for b in playerBullets:
            b.move()
            if b.checkOffScreen():
                playerBullets.pop(playerBullets.index(b))

        for a in asteroids:
            a.x += a.xv
            a.y += a.yv

            if (a.x >= player.x - player.w // 2 and a.x <= player.x + player.w // 2) or (
                    a.x + a.w <= player.x + player.w // 2 and a.x + a.w >= player.x - player.w // 2):
                if (a.y >= player.y - player.h // 2 and a.y <= player.y + player.h // 2) or (
                        a.y + a.h >= player.y - player.h // 2 and a.y + a.h <= player.y + player.h // 2):
                    health -= 1
                    asteroids.pop(asteroids.index(a))
                    if boolson:
                        GameConfig.Explosion_2.play()
                    break

            for b in playerBullets:
                if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                    if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                        if a.rank == 3:
                            if boolson:
                                GameConfig.Explosion_2.play()
                            score += 10
                            na1 = Meteorite(2)
                            na2 = Meteorite(2)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        elif a.rank == 2:
                            if boolson:
                                GameConfig.Explosion_1.play()
                            score += 20
                            na1 = Meteorite(1)
                            na2 = Meteorite(1)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        else:
                            score += 30
                            if boolson:
                                GameConfig.Explosion_1.play()
                        asteroids.pop(asteroids.index(a))
                        playerBullets.pop(playerBullets.index(b))
                        break

        for s in stars:
            s.x += s.xv
            s.y += s.yv
            if s.x < -100 - s.w or s.x > GameConfig.WINDOW_W + 100 or s.y > GameConfig.WINDOW_H + 100 or s.y < -100 - s.h:
                stars.pop(stars.index(s))
                break
            for b in playerBullets:
                if (b.x >= s.x and b.x <= s.x + s.w) or b.x + b.w >= s.x and b.x + b.w <= s.x + s.w:
                    if (b.y >= s.y and b.y <= s.y + s.h) or b.y + b.h >= s.y and b.y + b.h <= s.y + s.h:
                        bonus = True
                        bonus_init = count
                        stars.pop(stars.index(s))
                        playerBullets.pop(playerBullets.index(b))
                        break

        if health <= 0:
            gameover = True

        if bonus_init != -1:
            if count - bonus_init > 500:
                bonus = False
                bonus_init = -1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turnLeft()
        if keys[pygame.K_RIGHT]:
            player.turnRight()
        if keys[pygame.K_UP]:
            player.moveForward()
        if keys[pygame.K_SPACE]:
            if bonus:
                playerBullets.append(Tir())
                if boolson:
                    GameConfig.Tir.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not gameover:
                    if not bonus:
                        playerBullets.append(Tir())
                        if boolson:
                            GameConfig.Tir.play()
            if event.key == pygame.K_m:
                boolson = not boolson
            if event.key == pygame.K_TAB:
                if gameover:
                    gameover = False
                    health = 3
                    asteroids.clear()
                    aliens.clear()
                    alienBullets.clear()
                    stars.clear()
                    if score > meilleurScore:
                        meilleurScore = score
                    score = 0

    game_loop()


def main():
    pygame.quit()
    quit()


main()
