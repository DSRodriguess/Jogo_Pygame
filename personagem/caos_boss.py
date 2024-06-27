from .boss import Boss
import random 
from ataques.estalactite import Estalactite
from ataques.pilar import PilarDeFogo

class CaosBoss(Boss):
    def __init__(self, x, y):
        super().__init__(x, y, 100, 100, (148, 0, 211), 150)
        self.dano = 1

    def atacar(self, ataques, player):
        aux = random.randint(1,5)
        if(aux%2==0):
            ataques.append(Estalactite(player))
        else:
            ataques.append(PilarDeFogo(player))