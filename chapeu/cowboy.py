import pygame
from pygame.locals import *
from chapeu.chapeu import Chapeu

class Cowboy(Chapeu):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.cor = [
            (150,75,0),
            (218,165,32)
            ]
    
    def desenha_chapeu(self,scr):
        pygame.draw.rect(scr,self.cor[0],(self.x-5, self.y,60,5))

        pygame.draw.rect(scr,self.cor[0],(self.x-5, self.y-5,30,5))
        pygame.draw.rect(scr,self.cor[0],(self.x-5, self.y-10,13,5))

        pygame.draw.rect(scr,self.cor[0],(self.x+30, self.y-5,30,5))
        pygame.draw.rect(scr,self.cor[0],(self.x+47, self.y-10,13,5))

        pygame.draw.rect(scr,self.cor[0],(self.x+10, self.y-15,35,15))
        pygame.draw.rect(scr,self.cor[0],(self.x+10, self.y-20,10,15))
        pygame.draw.rect(scr,self.cor[0],(self.x+35, self.y-20,10,15))

        pygame.draw.rect(scr,self.cor[1],(self.x+10, self.y-10,35,5))