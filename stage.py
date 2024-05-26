import pygame

def grids(scr, altura, largura):
    for line in range(0, 6):
        pygame.draw.line(scr, (255,255,255), (0, line*200), (largura, line*200))
        pygame.draw.line(scr, (255,255,255), (line*200, 0), (line*200, altura))

