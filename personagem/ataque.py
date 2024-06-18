import pygame
import random

class Ataque:
    def __init__(self, largura_tela, altura_tela, player):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.largura = 30
        self.altura = 30
        self.color = (150, 75, 0)
        self.velocidade = 8
        self.x = random.randint(player.x - 50, player.x + 50) # Ataque começa aleatoriamente na posição do player
        self.y = -self.altura

    def update(self):
        self.y += self.velocidade

    def draw(self, scr):
        pygame.draw.rect(scr, self.color, (self.x, self.y, self.largura, self.altura))

    def checar_colisao(self, player):
        ataque_rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        player_rect = pygame.Rect(player.x, player.y, player.largura, player.altura)
        return ataque_rect.colliderect(player_rect)
