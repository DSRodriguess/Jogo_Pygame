import pygame
from pygame.locals import *
from sys import exit
from personagem.player import Player
from personagem.boss import Boss
from arma.escopeta import Escopeta
from arma.disco import Disco
from stage.stage import *
from ataques.estalactite import Estalactite 
from ataques.pilar import PilarDeFogo
from display_utils.moedas import mostrar_moedas
from display_utils.relogio import mostrar_relogio
from pprint import pprint
import os
import random

#Funcao debug, coloque a classe e suas variáveis serão printadas
#Deixa o jogo mais lento
def debugar(objeto):
    os.system('clear')
    pprint(vars(objeto))

pygame.init()
global_count =0
largura = 1000
altura = 800
scr = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("EDL GAME")

tile_size = 50
layout = [
        carregar_layout("./stage/layout1.txt"),
        carregar_layout("./stage/layout2.txt")
        ]

stage_atual = Stage(scr, layout[1])

# Cria o personagem passando (posição,tamanho, cor e vidas)
player = Player(150, 500, 50, 50, (0, 0, 255), 3)

boss_vivo = True
# Cria o Boss passando (posição,tamanho, cor e vidas)
boss = Boss(780, 600, 100, 100, (150, 75, 0), 100)

gun = Escopeta(player.x,player.y)
# gun = Disco(player.x,player.y)

# Tempo inicial
tempo_inicial = pygame.time.get_ticks()

# Moedas iniciais
moedas_iniciais = 100

# Tempo máximo em milissegundos (120 segundos)
tempo_maximo = 120 * 1000

# Função lambda para calcular o gold total
calcula_gold_total = lambda tempo, vidas: max(0, (moedas_iniciais - max(0, tempo - 20))) * vidas

# Lista para armazenar os ataques
ataques = []

# Temporizador para ataques
tempo_ultimo_ataque = pygame.time.get_ticks()
intervalo_ataques = 2000 

# Define a taxa de quadros
clock = pygame.time.Clock()
#fps = 60


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

    tempo_decorrido = pygame.time.get_ticks() - tempo_inicial
    tempo_restante = tempo_maximo - tempo_decorrido

    if boss_vivo:
        boss.draw(scr)

    if tempo_restante <= 0:
        print("Tempo esgotado! Fim de jogo.")

    
    # Atualizacao posicao arma com o personagem
    gun.x = player.x
    gun.y = player.y

    # Atualização tiros na tela e checagem de colisões
    gun.redesenha_tiro(scr, boss)

    # Eventos e Desenho da arma
    gun.event(keys,scr,global_count)
    gun.draw(scr)

    # Mostrar as moedas na tela
    mostrar_moedas(scr, player.moedas)

    # Mostrar o relógio com o tempo restante na tela
    mostrar_relogio(scr, tempo_restante, largura)
    
    #Colisão boss x Player
    boss.checa_dano_player(player)
    player.reseta_invencibilidade()

    #Posicao central player e boss
    player.atualiza_centro()
    boss.atualiza_centro()
    
    # Verifica se o boss foi derrotado
    if boss.vida <= 0 and boss_vivo:
        boss_vivo = False
        gold_total = calcula_gold_total(tempo_decorrido // 1000, player.vida)
        print(f"Boss derrotado! Você ganhou {gold_total} moedas.")
        player.moedas += gold_total
        
    # Gerar novos ataques
    if pygame.time.get_ticks() - tempo_ultimo_ataque > intervalo_ataques:
        #ataques.append(Estalactite(player))
        ataques.append(PilarDeFogo(player))
        tempo_ultimo_ataque = pygame.time.get_ticks()

    # Atualizar e desenhar ataques
    for ataque in ataques[:]:
        ataque.update()
        ataque.draw(scr)
        if ataque.checar_colisao(player):
            player.take_damage(1)
            player.recuar(75,ataque.x,ataque.y)
            ataques.remove(ataque)
        #elif ataque.y > altura:
        elif ataque.y < 100:
            ataques.remove(ataque)

    #Gravidade no player
    player.cair()

    #debug
    # debugar(player)

    pygame.display.update()
    #clock.tick(fps)
