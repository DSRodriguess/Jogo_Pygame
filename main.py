import pygame, sys
from stage import *

pygame.init()


#Definoções da tela
largura = 1000
altura = 800


scr = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("EDL GAME")

stage = stage(scr, altura, largura)

while True:
    scr.fill((1,1,0))
    stage.draw()
    grids(scr,altura,largura)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.KEYDOWN:
            key = pygame.key.name(ev.key)
            print(key," tecla Pressionada")
       # if ev.type == pygame.MOUSEMOTION:
            # pos = pygame.mouse.get_pos()
            # btn = pygame.mouse.get_pressed()
            # print("x {},y {}".format(pos[0],pos[1]))
    pygame.display.update()



