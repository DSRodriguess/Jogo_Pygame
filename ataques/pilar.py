import pygame
import random
from .ataque import Ataque
from pygame.locals import *

class PilarDeFogo(Ataque):
    def __init__(self, player):
        largura = 20
        altura = 50
        cor = (0, 255, 0)  
        x = player.x + random.randint(-player.largura // 2, player.largura // 2)
        y = 800
        super().__init__(x, y, largura, altura, cor)
        self.velocidade_subida = 1

    def update(self):
        self.y -= self.velocidade_subida
        if self.y + self.altura < 0:
            self.y = 0
