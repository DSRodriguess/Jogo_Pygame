import pygame
import random

class Ataque:
    def __init__(self, x, y, largura, altura, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor

    def draw(self, scr):
        pygame.draw.rect(scr, self.cor, (self.x, self.y, self.largura, self.altura))

    def checar_colisao(self, player):
        ataque_rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        player_rect = pygame.Rect(player.x, player.y, player.largura, player.altura)
        return ataque_rect.colliderect(player_rect)