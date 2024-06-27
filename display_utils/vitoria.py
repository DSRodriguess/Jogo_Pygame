import pygame
from pygame.locals import *
from sys import exit


def vitoria(scr, largura, altura,moedas):
    fonte = pygame.font.SysFont(None, 74)
    texto_titulo = fonte.render('Parabéns', True, (255, 255, 255))
    texto_comecar = fonte.render('Pressione Enter para reiniciar', True, (255, 255, 255))
    pontuacao = fonte.render(f"Moedas ganha:{moedas}", True, (255, 255, 255))

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rodando = False

        scr.fill((0, 0, 0))
        scr.blit(texto_titulo, ((largura - texto_titulo.get_width()) // 2, altura // 4))
        scr.blit(texto_comecar, ((largura - texto_comecar.get_width()) // 2, altura // 2))
        scr.blit(pontuacao, ((largura - pontuacao.get_width()) // 2, altura // 3))

        pygame.display.update()