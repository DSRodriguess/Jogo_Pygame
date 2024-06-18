import pygame
from pygame.locals import *
from chapeu.chapeu import Chapeu

class Nurse(Chapeu):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.cor = [
            (235,199,158), #Branco
            (255,0,0), #Vermelho
            ]
    
    def desenha_chapeu(self,scr):
        pygame.draw.rect(scr,self.cor[0],(self.x+20, self.y-15,30,15))
        pygame.draw.rect(scr,self.cor[0],(self.x+25, self.y-20,25,15))
        pygame.draw.rect(scr,self.cor[1],(self.x+35, self.y-10,15,3))
        pygame.draw.rect(scr,self.cor[1],(self.x+42, self.y-15,3,12))
    


