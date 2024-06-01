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
        self.tiros = []
        self.tempo_ultimo_tiro = 0


    def atira(self,scr,count):
        pass

    def draw(self,scr):
        pass

    def redesenha_tiro(self):
        for tiro in self.tiros:
            tiro['x'] += self.velocidade
            tiro['distancia'] +=self.velocidade
        #Se o tiro chegar no fim da tela ele sai da lista    
        #TODO mudar 1000 para o limite da tela
        self.tiros = [tiro for tiro in self.tiros if tiro['x'] < 1000 and tiro['distancia'] < self.alcance]

    def event(self, keys,scr,count):
        tempo_atual = pygame.time.get_ticks()
        if (keys[K_x] or keys[pygame.K_SPACE]) and (tempo_atual - self.tempo_ultimo_tiro > self.intervalo):
            self.atira()
