import pygame
from pygame.locals import *
from .personagem import Personagem

class Player(Personagem):
    def __init__(self, x, y, largura, altura, cor, vida=3):
        super().__init__(x, y, largura, altura, cor, vida)
        self.vidas_iniciais = vida
        self.rect = pygame.Rect(x, y, largura, altura)

    def move(self, keys, stage):
        dx, dy = 0, 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1.0
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = 1.0
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -1.0
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = 1.0

        self.rect.x += dx
        if stage.check_collision(self.rect):
            self.rect.x -= dx

        self.rect.y += dy
        if stage.check_collision(self.rect):
            self.rect.y -= dy

        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self, scr):
        super().draw(scr)
        self.draw_life_bar(scr)

    def draw_life_bar(self, scr):
        for i in range(self.vida):
            pygame.draw.rect(scr, (255, 0, 0), (10 + i*35, 10, 30, 10))

    def lose_life(self):
        if self.vida > 0:
            self.vida -= 1
        else:
            print("Game Over")

