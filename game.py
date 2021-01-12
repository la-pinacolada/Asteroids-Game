import pygame
import math
import random
from game_config import *
from player import *
from bonus import *
from meteorite import *
from ennemi import *

player = Player()


class Tir(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = player.cosinus
        self.s = player.sinus
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


def advance_state():
    GameConfig.window.blit(GameConfig.background, (0, 0))

    player.draw(GameConfig.window)
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


def game_loop():
    gameover = False
    bonus = False
    run = True
    while run:
        GameConfig.clock.tick(60)
        GameConfig.count += 1
        if not gameover:
            if GameConfig.count % 50 == 0:
                ran = random.choice([1, 1, 1, 2, 2, 3])
                GameConfig.asteroids.append(Meteorite(ran))
            if GameConfig.count % 1000 == 0:
                GameConfig.stars.append(Bonus())
            if GameConfig.count % 750 == 0:
                GameConfig.aliens.append(Ennemi())
            for i, a in enumerate(GameConfig.aliens):
                a.x += a.xv
                a.y += a.yv
                if a.x > GameConfig.WINDOW_W + 150 or a.x + a.w < -100 or a.y > GameConfig.WINDOW_H + 150 or a.y + a.h < -100:
                    GameConfig.aliens.pop(i)
                if GameConfig.count % 60 == 0:
                    GameConfig.alienBullets.append(TirEnnemi(a.x + a.w // 2, a.y + a.h // 2))

                for b in GameConfig.playerBullets:
                    if (b.x >= a.x and b.x <= a.x + a.w):
                        if (b.y >= a.y and b.y <= a.y + a.h):
                            GameConfig.aliens.pop(i)
                            GameConfig.score += 50
                            break

            player.updateLocation()
            for b in GameConfig.playerBullets:
                b.move()
                if b.checkOffScreen():
                    GameConfig.playerBullets.pop(GameConfig.playerBullets.index(b))

            for a in GameConfig.asteroids:
                a.x += a.xv
                a.y += a.yv

                if (a.x <= player.x + player.w // 2 and a.x >= player.x - player.w // 2):
                    if (a.y >= player.y - player.h // 2 and a.y <= player.y + player.h // 2):
                        GameConfig.health -= 1
                        GameConfig.asteroids.pop(GameConfig.asteroids.index(a))
                        break

                for b in GameConfig.playerBullets:
                    if (b.x >= a.x and b.x <= a.x + a.w):
                        if (b.y >= a.y and b.y <= a.y + a.h):
                            if a.rank == 3:
                                GameConfig.score += 10
                                na1 = Meteorite(2)
                                na2 = Meteorite(2)
                                na1.x = a.x
                                na2.x = a.x
                                na1.y = a.y
                                na2.y = a.y
                                GameConfig.asteroids.append(na1)
                                GameConfig.asteroids.append(na2)
                            elif a.rank == 2:
                                GameConfig.score += 20
                                na1 = Meteorite(1)
                                na2 = Meteorite(1)
                                na1.x = a.x
                                na2.x = a.x
                                na1.y = a.y
                                na2.y = a.y
                                GameConfig.asteroids.append(na1)
                                GameConfig.asteroids.append(na2)
                            else:
                                GameConfig.score += 30
                            GameConfig.asteroids.pop(GameConfig.asteroids.index(a))
                            GameConfig.playerBullets.pop(GameConfig.playerBullets.index(b))
                            break

            for s in GameConfig.stars:
                s.x += s.xv
                s.y += s.yv
                if s.x < -100 - s.w or s.x > GameConfig.WINDOW_W + 100 or s.y > GameConfig.WINDOW_H + 100 or s.y < -100 - s.h:
                    GameConfig.stars.pop(GameConfig.stars.index(s))
                    break
                for b in GameConfig.playerBullets:
                    if (b.x >= s.x and b.x <= s.x):
                        if (b.y >= s.y and b.y <= s.y):
                            bonus = True
                            bonus_init = GameConfig.count
                            GameConfig.stars.pop(GameConfig.stars.index(s))
                            GameConfig.playerBullets.pop(GameConfig.playerBullets.index(b))
                            break

            if GameConfig.health <= 0:
                gameover = True

            if GameConfig.bonus_init != -1:
                if GameConfig.count - GameConfig.bonus_init > 500:
                    bonus = False
                    GameConfig.bonus_init = -1

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.turnLeft()
            if keys[pygame.K_RIGHT]:
                player.turnRight()
            if keys[pygame.K_UP]:
                player.moveForward()
            if keys[pygame.K_SPACE]:
                if bonus:
                    GameConfig.playerBullets.append(Tir())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not gameover:
                        if not bonus:
                            GameConfig.playerBullets.append(Tir())
                if event.key == pygame.K_TAB:
                    if gameover:
                        gameover = False
                        GameConfig.health = 3
                        GameConfig.asteroids.clear()
                        GameConfig.aliens.clear()
                        GameConfig.alienBullets.clear()
                        GameConfig.stars.clear()
                        if GameConfig.score > GameConfig.meilleurScore:
                            GameConfig.meilleurScore = GameConfig.score
                        GameConfig.score = 0
        font = pygame.font.SysFont('serif sans ms', 40)
        HealthText = font.render('Health : ' + str(GameConfig.health), 1, (204, 197, 185))
        ScoreText = font.render('Score Actuel : ' + str(GameConfig.score), 1, (204, 197, 185))
        MeilleurScoreText = font.render('Meilleur Score : ' + str(GameConfig.meilleurScore), 1, (204, 197, 185))
        TryAgainText = font.render('Game Over ( Press Tab to try again)', 1, (204, 197, 185))

        if bonus:
            pygame.draw.rect(GameConfig.window, (0, 0, 0), [GameConfig.WINDOW_W // 2 - 51, 19, 102, 22])
            pygame.draw.rect(GameConfig.window, (255, 255, 255),
                             [GameConfig.WINDOW_W // 2 - 50, 20, 100 - 100 * (GameConfig.count - bonus_init) / 500, 20])

        if gameover:
            GameConfig.window.blit(TryAgainText,
                                   (GameConfig.WINDOW_W // 2 - TryAgainText.get_width() // 2,
                                    GameConfig.WINDOW_H // 2 - TryAgainText.get_height() // 2))
        GameConfig.window.blit(HealthText, (25, 25))
        GameConfig.window.blit(ScoreText, (25, 35 + HealthText.get_height()))
        GameConfig.window.blit(MeilleurScoreText, (25, 45 + HealthText.get_height() + ScoreText.get_height()))
        pygame.display.update()
        advance_state()


game_loop()


def main():
    pygame.init()
    GameConfig.init()
    window = pygame.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H))
    pygame.display.set_caption("Arcade Asteroids")
    pygame.quit()
    quit()


main()
