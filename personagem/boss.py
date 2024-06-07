import pygame
from pygame.locals import *
from .personagem import Personagem

class Boss(Personagem):
    def __init__(self, x, y, largura, altura, cor, vida):
        super().__init__(x, y, largura, altura, cor, vida)
        self.vida_max = vida
        self.dano = 1
    
    def draw(self, scr):
        super().draw(scr)
        self.draw_hp_bar(scr)
    
    def draw_hp_bar(self, scr):
        # Calcula a largura da barra de HP proporcional à vida atual
        hp_bar_width = self.largura * (self.vida / self.vida_max)
        hp_bar_height = 5  # Altura da barra de HP
        hp_bar_x = self.x
        hp_bar_y = self.y - 10  # Coloca a barra de HP um pouco acima do Boss

        # Desenha a barra de HP com duas partes: fundo e vida atual
        pygame.draw.rect(scr, (255, 0, 0), (hp_bar_x, hp_bar_y, self.largura, hp_bar_height))  # Fundo vermelho
        pygame.draw.rect(scr, (0, 255, 0), (hp_bar_x, hp_bar_y, hp_bar_width, hp_bar_height))  # Vida verde
    
    def take_damage(self, amount):
        self.vida -= amount
        if self.vida < 0:
            self.vida = 0

    def checar_colisao(self, player):
        player_rect = pygame.Rect(player.x, player.y, player.largura, player.altura)
        boss_rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        return boss_rect.colliderect(player_rect)
    
    def checa_dano_player(self,player):
        if self.checar_colisao(player):
            player.tempo_ultimo_dano = pygame.time.get_ticks()
            player.recuar(75,self.x,self.y)
            # player.x = self.x - player.largura -50 #recuo do player
            if player.invencivel == False:
                player.take_damage(self.dano)

