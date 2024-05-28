import pygame
from pygame.locals import *
from arma.arma import Arma

class Disco(Arma):
    def __init__(self,x,y):
        self.cor = (255,165,0)
        self.velocidade = 0.70
        self.dano = 3
        self.alcance = 10 #10% da tela

    def draw(self,scr):
        pygame.draw.circle(scr,self.cor,(self.x+55, self.y+20),15)
    
    def atira(self,scr,count):
            pygame.draw.circle(scr,self.cor,(self.x+55+(count), self.y+20),15)
         
    def event(self, keys,scr,count):
        if keys[K_x] or keys[pygame.K_SPACE]:
            self.atira(scr,count)
        