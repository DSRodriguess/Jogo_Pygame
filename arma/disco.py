import pygame
from pygame.locals import *
from arma.arma import Arma

class Disco(Arma):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.cor = (255,165,0)
        self.velocidade = 1.2
        self.dano = 5
        self.alcance = 300 
        self.intervalo = 500
        self.raio = 20

    def draw(self,scr):
        pygame.draw.circle(scr,self.cor,(self.x+55, self.y+20),15)
        for tiro in self.tiros:
            pygame.draw.circle(scr,self.cor,(tiro['x'],tiro['y']),self.raio)
            

    def atira(self):
        self.tiros.append({'x':self.x+50, 'y':self.y+15,'distancia':0})
        self.tempo_ultimo_tiro = pygame.time.get_ticks()
