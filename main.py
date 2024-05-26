import pygame, sys
from stage import grids

pygame.init()


#Definoções da tela
largura = 1000
altura = 1000


scr = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("EDL GAME")

while True:
    scr.fill((1,1,0))
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




