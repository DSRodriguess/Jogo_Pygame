import pygame
from pygame.locals import *
from sys import exit
from personagem.personagem import Personagem
from personagem.player import Player
from personagem.boss import Boss
from arma.escopeta import Escopeta
from arma.disco import Disco
from stage.stage import *
from pprint import pprint
import os

#Funcao debug, coloque a classe e suas variáveis serão printadas
#Deixa o jogo mais lento
def debugar(objeto):
    os.system('clear')
    pprint(vars(objeto))

pygame.init()

#Definições da tela
largura = 1000
altura = 800
global_count = 0
scr = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("EDL GAME")

tile_size = 50
layout = [
        carregar_layout("./stage/layout1.txt"),
        carregar_layout("./stage/layout2.txt")
        ]

stage_atual = Stage(scr, layout[1])

player = Player(150, 500, 50, 50, (0, 0, 255), 3)

boss_vivo = True
boss = Boss(780, 600, 100, 100, (150, 75, 0), 100)

gun = Escopeta(player.x,player.y)
# gun = Disco(player.x,player.y)

tempo_inicial = pygame.time.get_ticks()

def mostrar_relogio(scr, tempo_decorrido):
    font = pygame.font.Font(None, 36)
    segundos = tempo_decorrido // 1000
    minutos = segundos // 60
    horas = minutos // 60
    tempo_formatado = "{:02d}:{:02d}:{:02d}".format(horas, minutos % 60, segundos % 60)
    text = font.render(f"Tempo: {tempo_formatado}", 1, (10, 10, 10))
    text_rect = text.get_rect()
    text_rect.topright = (largura - 10, 10)  
    scr.blit(text, text_rect)

terra =[player]
pressionando = False
while True:
    scr.fill((255,255,255)) 
    stage_atual.draw()
    grids(scr,altura,largura)

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
        if ev.type == pygame.KEYDOWN:
            key = pygame.key.name(ev.key)
            # print(key, "tecla Pressionada")
            pressionando = True
        if ev.type == pygame.KEYUP:
            key = pygame.key.name(ev.key)
            # print(key, "tecla Solta")
            pressionando = False

    keys = pygame.key.get_pressed()
    player.move(keys,stage_atual,pressionando)
    player.draw(scr)

    if boss_vivo:
        boss.draw(scr)


    #Atualizacao posicao arma com o personagem
    gun.x = player.x
    gun.y = player.y

    # Atualização tiros na tela e checagem de colisões
    gun.redesenha_tiro(scr, boss)

    #Eventos e Desenho da arma
    gun.event(keys,scr,global_count)
    gun.draw(scr)


    mostrar_relogio(scr, pygame.time.get_ticks() - tempo_inicial)
    
    #Colisão boss x Player
    boss.checa_dano_player(player)
    player.reseta_invencibilidade()

    #Posicao central player e boss
    player.atualiza_centro()
    boss.atualiza_centro()

    #Gravidade no player
    player.cair()

    #debug
    # debugar(player)
    
    pygame.display.update()
