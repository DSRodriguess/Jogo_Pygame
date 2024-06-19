import pygame
import random
from .ataque import Ataque
from pygame.locals import *

class PilarDeFogo(Ataque):
    def __init__(self, player):
        x = 0
        y = 0
        largura = 20
        altura = 0
        cor = (255, 0, 0) 
        super().__init__(x, y, largura, altura, cor)
        self.velocidade = 5
        self.altura_maxima = 100  # Altura máxima do pilar

    def update(self):
        self.y += self.velocidade