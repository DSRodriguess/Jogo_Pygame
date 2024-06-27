import pygame

# Função para mostrar as moedas na tela
def mostrar_moedas(scr, moedas):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Moedas: {moedas}", 1, (10, 10, 10))
    scr.blit(text, (10, 50))