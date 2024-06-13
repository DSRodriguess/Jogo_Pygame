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

    def gravidade(coisa):
        # if(object.gravidade == True):
        coisa.y += 1
        coisa.rect.y += 1
        coisa.draw(scr)
        return coisa

    print(map(gravidade,terra))
    #print(player.y)
    #Gravidade




    # l = [1,2,3,4]
    # def dobro(x):
    #     return x*2
    # dobrado = (map(dobro,l))
    # dobrado = list(dobrado)
    # print(dobrado)

    keys = pygame.key.get_pressed()
    player.move(keys,stage)
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
    boss.checa_dano_player(player)
    player.reseta_invencibilidade()
    player.atualiza_centro()
    boss.atualiza_centro()
    # player.cair()
    pygame.display.update()
