import pygame
from pygame.locals import *
from arma.arma import Arma


class Escopeta(Arma):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.cor = (128,128,128)
        self.velocidade = 2
        self.dano = 12
        self.alcance = 200 #30% da tela
        self.intervalo = 700 #taxa de tiros em milisegundos
        self.largura_tiro = 5
        self.altura_tiro = 5


    def draw(self,scr):
        pygame.draw.rect(scr,self.cor,(self.x+40, self.y+20,40,5))
        pygame.draw.rect(scr,(150,75,0),(self.x+50, self.y+20,15,8))
        pygame.draw.rect(scr,self.cor,(self.x+40, self.y+20,5,15))
        #for tiro in self.tiros:
             #pygame.draw.rect(scr,(0,0,0),(tiro['x'],tiro['y'],self.largura_tiro,self.altura_tiro))

    def atira(self):
            self.tiros.append({'x':self.x+65, 'y':self.y+15,'distancia':0})
            self.tiros.append({'x':self.x+65, 'y':self.y+25,'distancia':0})
            self.tempo_ultimo_tiro = pygame.time.get_ticks()




