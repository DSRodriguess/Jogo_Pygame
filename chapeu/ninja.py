import pygame
from pygame.locals import *
from chapeu.chapeu import Chapeu

class Ninja(Chapeu):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.cor = [
            (0,0,0), #Preto
            (192,192,192), #Cinza
            (13,33,79) #Azul
            ]
    
    def desenha_chapeu(self,scr):
        pygame.draw.rect(scr,self.cor[2],(self.x, self.y,50,15))
        pygame.draw.rect(scr,self.cor[1],(self.x+30, self.y+2,20,12))
        pygame.draw.rect(scr,self.cor[0],(self.x+40, self.y+5,2,8))
        pygame.draw.rect(scr,self.cor[0],(self.x+43, self.y+5,2,8))
        pygame.draw.rect(scr,self.cor[0],(self.x+46, self.y+5,2,8))
        pygame.draw.rect(scr,self.cor[0],(self.x+38, self.y+7,8,2))



