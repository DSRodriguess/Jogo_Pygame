from .boss import Boss
from ataques.estalactite import Estalactite

class TerraBoss(Boss):
    def __init__(self, x, y):
        super().__init__(x, y, 100, 100, (150, 75, 0), 150)
        self.dano = 1

    def atacar(self, ataques, player):
        ataques.append(Estalactite(player))