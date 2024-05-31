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

    def draw(self, scr):
        pygame.draw.rect(scr, self.cor, (self.x, self.y, self.largura, self.altura))
    
    def move(self, keys):
        if keys[K_a] or keys[pygame.K_LEFT]:
            self.x -= 0.25
        if keys[K_d] or keys[pygame.K_RIGHT]:
            self.x += 0.25
        if keys[K_w] or keys[pygame.K_UP]:
            self.y -= 0.25
        if keys[K_s] or keys[pygame.K_DOWN]:
            self.y += 0.25
