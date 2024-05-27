import pygame
from pygame.locals import *

class Arma:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.cor = (128,128,128)
        self.velocidade = 0.25
        self.dano = 1
        self.alcance = 30#30% da tela

    def draw(self,scr):
        pygame.draw.rect(scr,self.cor,(self.x+40, self.y+20,30,5))
    
    def move(self, keys):
        if keys[K_a] or keys[pygame.K_LEFT]:
            self.x -= 0.25
        if keys[K_d] or keys[pygame.K_RIGHT]:
            self.x += 0.25
        if keys[K_w] or keys[pygame.K_UP]:
            self.y -= 0.25
        if keys[K_s] or keys[pygame.K_DOWN]:
            self.y += 0.25
