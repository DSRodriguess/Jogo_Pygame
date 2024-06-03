import pygame
from pygame.locals import *
from arma.arma import Arma


class Escopeta(Arma):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.cor = (128,128,128)
        self.velocidade = 2
        self.dano = 1
        self.alcance = 200 #30% da tela
        self.intervalo = 700 #taxa de tiros em milisegundos
        self.largura_tiro = 5
        self.altura_tiro = 5


    def draw(self,scr):
        pygame.draw.rect(scr,self.cor,(self.x+40, self.y+20,30,5))
        for tiro in self.tiros:
             pygame.draw.rect(scr,(0,0,0),(tiro['x'],tiro['y'],self.largura_tiro,self.altura_tiro))

    def atira(self):
            self.tiros.append({'x':self.x+50, 'y':self.y+15,'distancia':0})
            self.tiros.append({'x':self.x+50, 'y':self.y+25,'distancia':0})
            self.tempo_ultimo_tiro = pygame.time.get_ticks()
