import pygame
from pygame.locals import *
from chapeu.chapeu import Chapeu

class Mugi(Chapeu):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.cor = [
            (207,181,59),#Beje
            (255,0,0),#Marrom

            ]
    
    def desenha_chapeu(self,scr):
        pygame.draw.rect(scr,self.cor[0],(self.x-5, self.y,60,5))
        pygame.draw.rect(scr,self.cor[0],(self.x+10, self.y-15,35,15))
        pygame.draw.rect(scr,self.cor[1],(self.x+10, self.y-10,35,5))
        pygame.draw.rect(scr,self.cor[0],(self.x+12, self.y-20,28,5))