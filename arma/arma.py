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

    def checar_colisao(self, tiro, boss):
        tiro_rect = pygame.Rect(tiro['x'], tiro['y'], 5, 5) 
        boss_rect = pygame.Rect(boss.x, boss.y, boss.largura, boss.altura)
        return tiro_rect.colliderect(boss_rect)


    def redesenha_tiro(self, scr, boss):
        for tiro in self.tiros:
            tiro['x'] += self.velocidade
            tiro['distancia'] += self.velocidade

            pygame.draw.rect(scr, (0, 0, 0), (tiro['x'], tiro['y'], 5, 5))  # Desenha os tiros
            if self.checar_colisao(tiro, boss): 
                boss.take_damage(self.dano)
                self.tiros.remove(tiro)
            elif tiro['distancia'] > self.alcance:
                self.tiros.remove(tiro)

    def event(self, keys, scr, count):
        tempo_atual = pygame.time.get_ticks()
        if (keys[K_x] or keys[pygame.K_SPACE]) and (tempo_atual - self.tempo_ultimo_tiro > self.intervalo):
            self.atira()