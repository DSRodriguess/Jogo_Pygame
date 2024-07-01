import pygame

class Stage():
    def __init__(self, scr, stage, tile_size=50):
        self.scr = scr
        self.stage = stage
        self.tile_size = tile_size

    def draw(self):
        for row in range(0, 16):
            for col in range(0, 20):
                if self.stage[row][col] == 1:
                    pygame.draw.rect(self.scr, (255,0,0), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                if self.stage[row][col] == 2:
                    pygame.draw.rect(self.scr, (100,100,0), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                if self.stage[row][col] == 3:
                    pygame.draw.rect(self.scr, (100,100,100), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
    def checar_colisao(self, rect):
        for row in range(0, 16):
            for col in range(0, 20):
                if self.stage[row][col] == 1:
                    wall = pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
                    if rect.colliderect(wall):
                        return True
        return False

def carregar_layout(filename):
    stage = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split(',')))
            stage.append(row)
    return stage

def grids(scr, altura, largura,tile_size=50):
    for line in range(0, 20):
        pygame.draw.line(scr, (255,255,255), (0, line*tile_size), (largura, line*50))
        pygame.draw.line(scr, (255,255,255), (line*tile_size, 0), (line*tile_size, altura))

