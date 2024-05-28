import pygame
from pygame.locals import *

class Arma:
    def __init__(self,x,y):
        self.x = x #posicao x do personagem
        self.y = y #posicao y do personagem
        self.cor = (255,255,255) 
        self.velocidade = 0 
        self.dano = 0
        self.alcance = 0 

    def atira(self,scr,count):
        pass

    def draw(self,scr):
        pass
    
    def event(self, keys,scr,count):
        pass