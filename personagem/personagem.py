import pygame
from pygame.locals import *

class Personagem:
    def __init__(self, x, y, largura, altura, cor, vida):
        self.largura = largura
        self.altura = altura
        self.x = x
        self.y = y
        self.cor = cor
        self.vida = vida
        self.centro = (self.x+(self.largura/2),self.y+(self.altura/2))
        self.gravidade = True
        self.limite_pulo = 150
        self.pulando = False
        self.altura_ultimo_pulo = 0
        self.chapeu = False

    def draw(self, scr):
        pygame.draw.rect(scr, self.cor, (self.x, self.y, self.largura, self.altura))
        if(self.chapeu):
            self.chapeu.desenha_chapeu(scr)

    def take_damage(self, amount):
        pass

    def atualiza_centro(self):
        self.centro = self.x+(self.largura/2),self.y+(self.altura/2)

    def pular(self):
        pass

    def cair(self):
        if (self.gravidade == True):
            self.y +=1
            self.rect.y +=1
        else:
            pass
        

