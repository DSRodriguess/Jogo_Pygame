import pygame

# Função para mostrar o relógio na tela
def mostrar_relogio(scr, tempo_decorrido, largura):
    font = pygame.font.Font(None, 36) 
    segundos = tempo_decorrido // 1000
    minutos = segundos // 60
    tempo_formatado = "{:02d}:{:02d}".format(minutos % 60, segundos % 60)
    text = font.render(f"Tempo: {tempo_formatado}", 1, (10, 10, 10))
    text_rect = text.get_rect()
    text_rect.topright = (largura - 10, 10)  
    scr.blit(text, text_rect)