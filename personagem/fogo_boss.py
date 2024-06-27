from .boss import Boss
from ataques.pilar import PilarDeFogo


class FogoBoss(Boss):
    def __init__(self, x, y):
        super().__init__(x, y, 100, 100, (114, 47, 55), 150)
        self.dano = 1

    def atacar(self, ataques, player):
        ataques.append(PilarDeFogo(player))
