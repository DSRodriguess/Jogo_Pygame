import pygame
from pygame.locals import *
from arma.arma import Arma


class Escopeta(Arma):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.cor = (128,128,128)
        self.velocidade = 0.25
        self.dano = 1
        self.alcance = 30 #30% da tela

    def draw(self,scr):
        pygame.draw.rect(scr,self.cor,(self.x+40, self.y+20,30,5))

    def atira(self,scr,count):
            pygame.draw.rect(scr,(0,0,0),(self.x+50+(count), self.y+18,10,10))

    def event(self, keys,scr,count):
        super().event(keys,scr,count)
        if keys[K_x] or keys[pygame.K_SPACE]:
            self.atira(scr,count)

