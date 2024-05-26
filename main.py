import pygame, sys
from pygame.locals import *
from sys import exit
from personagem.personagem import Personagem

pygame.init()

altura = 500
largura = 500

scr = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("EDL GAME")

player = Personagem(50, 50, 50, 50, (0, 0, 255))

while True:
    scr.fill((0,0,0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.KEYDOWN:
            key = pygame.key.name(ev.key)
            print(key, "tecla Pressionada")
        if ev.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            # btn = pygame.mouse.get_pressed()
            print("x {},y {}".format(pos[0], pos[1]))

    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw(scr)

    pygame.display.update()
