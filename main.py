import pygame
from pygame.locals import *
from sys import exit
from pprint import pprint
import os

#------------------------------------Player------------------------------------
from personagem.player import Player

from chapeu.chapeu import Chapeu
from chapeu.cowboy import Cowboy
from chapeu.ninja import Ninja
from chapeu.nurse import Nurse
from chapeu.russo import Russo
from chapeu.mugi import Mugi
#------------------------------------Armas------------------------------------
from arma.pistola import Pistola
from arma.escopeta import Escopeta
from arma.metralhadora import Metralhadora
from arma.disco import Disco
from arma.chamas import Chamas
#------------------------------------Boss------------------------------------
from personagem.boss import Boss
from personagem.ataque import Ataque
#------------------------------------Cenario------------------------------------
from stage.stage import *


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

gun = Pistola(player.x,player.y)
# gun = Escopeta(player.x,player. y )
# gun = Metralhadora(player.x,player.y)
# gun = Disco(player.x,player.y)
# gun = Chamas(player.x,player.y)

hat=0
hat = Cowboy(player.x,player.y)
# hat = Ninja(player.x,player.y)
# hat = Nurse(player.x,player.y)
# hat = Russo(player.x,player.y)
# hat = Mugi(player.x,player.y)

if(hat):
    player.chapeu = hat

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
intervalo_ataques = 700  # 2 segundos

# Função para mostrar as moedas na tela
def mostrar_moedas(scr, moedas):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Moedas: {moedas}", 1, (10, 10, 10))
    scr.blit(text, (10, 50))

# Função para mostrar o relógio na tela
def mostrar_relogio(scr, tempo_decorrido):
    font = pygame.font.Font(None, 36) 
    segundos = tempo_decorrido // 1000
    minutos = segundos // 60
    tempo_formatado = "{:02d}:{:02d}".format(minutos % 60, segundos % 60)
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

    tempo_decorrido = pygame.time.get_ticks() - tempo_inicial
    tempo_restante = tempo_maximo - tempo_decorrido

    if boss_vivo:
        boss.draw(scr)

    if tempo_restante <= 0:
        print("Tempo esgotado! Fim de jogo.")

    
    # Atualizacao posicao arma com o personagem
    gun.x = player.x
    gun.y = player.y 

    if(player.chapeu):
        hat.x = player.x
        hat.y = player.y

    # Atualização tiros na tela e checagem de colisões
    gun.redesenha_tiro(scr, boss)

    # Eventos e Desenho da arma
    gun.event(keys,scr,global_count)
    gun.draw(scr)

    # Mostrar as moedas na tela
    mostrar_moedas(scr, player.moedas)

    # Mostrar o relógio com o tempo restante na tela
    mostrar_relogio(scr, tempo_restante)
    
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
    if(boss_vivo):
        if pygame.time.get_ticks() - tempo_ultimo_ataque > intervalo_ataques:
            ataques.append(Ataque(largura, altura, player))
            tempo_ultimo_ataque = pygame.time.get_ticks()
    
 
    # Atualizar e desenhar ataques
    for ataque in ataques[:]:
        ataque.update()
        ataque.draw(scr)
        if ataque.checar_colisao(player):
            player.take_damage(1)
            player.recuar(75,ataque.x,ataque.y)
            ataques.remove(ataque)
        elif ataque.y > altura:
            ataques.remove(ataque)

    #Gravidade no player
    player.cair()

    #debug
    # debugar(player)
    
    pygame.display.update()
