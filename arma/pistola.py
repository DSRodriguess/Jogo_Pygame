import pygame
from pygame.locals import *
from arma.arma import Arma


class Pistola(Arma):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.cor = (192,192,192)
        self.velocidade = 5
        self.dano = 5
        self.alcance = 300 #30% da tela
        self.intervalo = 500 #taxa de tiros em milisegundos
        self.largura_tiro = 10
        self.altura_tiro = 10


    def draw(self,scr):
        pygame.draw.rect(scr,self.cor,(self.x+50, self.y+20,20,5))
        pygame.draw.rect(scr,self.cor,(self.x+50, self.y+20,5,15))
        # pygame.draw.rect(scr,self.cor,(self.x+10, self.y+30,10,15))
        #for tiro in self.tiros:
             #pygame.draw.rect(scr,(0,0,0),(tiro['x'],tiro['y'],self.largura_tiro,self.altura_tiro))

    def atira(self):
            self.tiros.append({'x':self.x+65, 'y':self.y+20,'distancia':0})
            self.tempo_ultimo_tiro = pygame.time.get_ticks()




