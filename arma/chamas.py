import pygame
from pygame.locals import *
from arma.arma import Arma


class Chamas(Arma):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.cor = (255,0,0)
        self.velocidade = 3
        self.dano = 2
        self.alcance = 200 #30% da tela
        self.intervalo = 70 #taxa de tiros em milisegundos
        self.raio = 30


    def draw(self,scr):
        pygame.draw.circle(scr,self.cor,(self.x+50, self.y+20),5)

        for tiro in self.tiros:
            pygame.draw.circle(scr,self.cor,(tiro['x'],tiro['y']),self.raio)          

    def atira(self):
            self.tiros.append({'x':self.x+65, 'y':self.y+20,'distancia':0})
            self.tempo_ultimo_tiro = pygame.time.get_ticks()

    # def event(self, keys, scr, count):
    #     tempo_atual = pygame.time.get_ticks() #TODO VAI PARA CLASSE GLBOAL
    #     if (keys[K_x] or keys[pygame.K_SPACE]):
    #         self.atira()



