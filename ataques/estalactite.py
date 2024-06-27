import pygame
import random
from .ataque import Ataque
from pygame.locals import *


class Estalactite(Ataque):
    def __init__(self, player):
        x = player.x + random.randint(-50, 50)
        y = 0
        largura = 20
        altura = 20
        cor = (150, 75, 0) 
        super().__init__(x, y, largura, altura, cor)
        self.velocidade = 5

    def update(self):
        self.y += self.velocidade
