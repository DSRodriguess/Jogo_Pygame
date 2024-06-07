import pygame
from pygame.locals import *
from .personagem import Personagem

class Player(Personagem):
    def __init__(self, x, y, largura, altura, cor, vida=3):
        super().__init__(x, y, largura, altura, cor, vida)
        self.vidas_iniciais = vida
        self.moedas = 0 
        
    def move(self, keys):
        if keys[K_a] or keys[pygame.K_LEFT]:
            self.x -= 1.0
        if keys[K_d] or keys[pygame.K_RIGHT]:
            self.x += 1.0
        if keys[K_w] or keys[pygame.K_UP]:
            self.y -= 1.0
        if keys[K_s] or keys[pygame.K_DOWN]:
            self.y += 1.0

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

