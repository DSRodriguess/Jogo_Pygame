import pygame
from pygame.locals import *

class Personagem:
    def __init__(self, x, y, largura, altura, cor, vida):
        self.largura = largura
        self.altura = altura
        self.x = x
        self.y = y
        self.cor = cor
        self.vida = vida
        self.centro = (self.x+(self.largura/2),self.y+(self.altura/2))

    def draw(self, scr):
        pygame.draw.rect(scr, self.cor, (self.x, self.y, self.largura, self.altura))

    def take_damage(self, amount):
        pass

    def atualiza_centro(self):
        self.centro = self.x+(self.largura/2),self.y+(self.altura/2)
