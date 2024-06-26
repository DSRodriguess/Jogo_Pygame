from .boss import Boss
from ataques.estalactite import Estalactite
from ataques.pilar import PilarDeFogo

class CaosBoss(Boss):
    def __init__(self, x, y):
        super().__init__(x, y, 100, 100, (148, 0, 211), 150)
        self.dano = 1

    def atacar(self, ataques, player):
        ataques.append(Estalactite(player))
        ataques.append(PilarDeFogo(player))