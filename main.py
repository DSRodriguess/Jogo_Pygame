import pygame
from pygame.locals import *
from sys import exit
from personagem.personagem import Personagem
from personagem.player import Player
from personagem.boss import Boss
from arma.arma import Arma
from arma.escopeta import Escopeta
from arma.disco import Disco
from stage import *

pygame.init()

#Definoções da tela
largura = 1000
altura = 800
global_count = 0
scr = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("EDL GAME")

stage = stage(scr, altura, largura)

player = Player(150, 650, 50, 50, (0, 0, 255), 3)
boss = Boss(780, 600, 100, 100, (150, 75, 0), 100)
gun = Escopeta(player.x,player.y)
# gun = Disco(player.x,player.y)

while True:
    scr.fill((255,255,255)) 
    stage.draw()
    grids(scr,altura,largura)

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
        if ev.type == pygame.KEYDOWN:
            key = pygame.key.name(ev.key)
            print(key, "tecla Pressionada")


    keys = pygame.key.get_pressed()

    player.move(keys)
    player.draw(scr)
    pygame.draw.lines(scr,(0,255,0),False,(player.centro,boss.centro))
    boss.draw(scr)
    #Atualizacao posicao arma com o personagem
    gun.x = player.x
    gun.y = player.y

    # Atualização tiros na tela e checagem de colisões
    gun.redesenha_tiro(scr, boss)

    #Eventos e Desenho da arma
    gun.event(keys,scr,global_count)
    gun.draw(scr)

    boss.checa_dano_player(player)
    player.reseta_invencibilidade()
    player.atualiza_centro()
    boss.atualiza_centro()
    
    pygame.display.update()
