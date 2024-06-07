import pygame
from pygame.locals import *
from .personagem import Personagem

class Player(Personagem):
    def __init__(self, x, y, largura, altura, cor, vida=3):
        super().__init__(x, y, largura, altura, cor, vida)
        self.vidas_iniciais = vida
        self.tempo_ultimo_dano = 0
        self.tempo_invencibilidade = 1000 #1000ms = 1s
        self.invecivel = False
        
    def move(self, keys):
        if keys[K_a] or keys[pygame.K_LEFT]:
            self.x -= 1.0
        if keys[K_d] or keys[pygame.K_RIGHT]:
            self.x += 1.0
        if keys[K_w] or keys[pygame.K_UP]:
            self.y -= 1.0
        if keys[K_s] or keys[pygame.K_DOWN]:
            self.y += 1.0

    def draw(self, scr):
        super().draw(scr)
        self.draw_life_bar(scr)

    def draw_life_bar(self, scr):
        for i in range(self.vida):
            pygame.draw.rect(scr, (255, 0, 0), (10 + i*35, 10, 30, 10))

    def reseta_invencibilidade(self):
        tempo_atual = pygame.time.get_ticks()
        if (tempo_atual - self.tempo_ultimo_dano > self.tempo_invencibilidade):
            self.invencivel = False

    def take_damage(self, amount):
        if (self.invecivel == False):
            self.vida -= amount
            self.invencivel = True
        if (self.vida < 0):
            print("Game Over")

    def recuar(self,distancia,x_boss,y_boss):
        if(self.x < x_boss):
            self.x -= distancia
        else:
            self.x += distancia

        if(self.y <= y_boss):
            self.y -= distancia



        # self.y -= distancia
        # m = ((self.y - y_boss)/(self.x-x_boss))
        # self.y = m * (self.x - x_boss) + y_boss
        # self.x -= distancia
    

