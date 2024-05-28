import pygame, sys
from pygame.locals import *
from sys import exit
from personagem.personagem import Personagem
from arma.arma import Arma
from arma.escopeta import Escopeta
from arma.disco import Disco

pygame.init()

altura = 500
largura = 500
global_count = 0
scr = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("EDL GAME")

player = Personagem(50, 50, 50, 50, (0, 0, 255))
# gun = Escopeta(player.x,player.y)
gun = Disco(player.x,player.y)

while True:
    scr.fill((255,255,255)) 
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

    global_count += 1 
    if global_count > max(altura,largura) : global_count = 0

    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw(scr)

    #Atualizacao posicao arma com o personagem
    gun.x = player.x
    gun.y = player.y

    #Atualização tiros na tela
    gun.redesenha_tiro()

    #Eventos e Desenho da arma
    gun.event(keys,scr,global_count)
    gun.draw(scr)
    
    pygame.display.update()
