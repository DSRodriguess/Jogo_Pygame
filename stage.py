import pygame

tile_size = 50

stage_1 = [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

class stage():
    def __init__(self, scr, altura, largura):
        self.scr = scr
        self.altura = altura
        self.largura = largura
        self.stage = stage_1

    def draw(self):
        for row in range(0, 16):
            for col in range(0, 20):
                if self.stage[row][col] == 1:
                    pygame.draw.rect(self.scr, (255,0,0), (col*tile_size, row*tile_size, tile_size, tile_size))

    def check_collision(self, rect):
        for row in range(0, 16):
            for col in range(0, 20):
                if self.stage[row][col] == 1:
                    wall = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
                    if rect.colliderect(wall):
                        return True
        return False


def grids(scr, altura, largura):
    for line in range(0, 20):
        pygame.draw.line(scr, (255,255,255), (0, line*tile_size), (largura, line*50))
        pygame.draw.line(scr, (255,255,255), (line*tile_size, 0), (line*tile_size, altura))

