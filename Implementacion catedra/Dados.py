import random
DEFAULTS = (1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6)


def resultado_dado(probabilidades):
    u = random.random()
    value = 0
    prob_acum = 0
    while u > prob_acum:
        prob_acum += probabilidades[value]
        value += 1
    return value

class Dados(object):
    def __init__(self, probabilidades = (DEFAULTS, DEFAULTS)):
        self.dados = probabilidades
        
    def lanzar(self):
        resul = 0
        for dado in self.dados:
            resul += resultado_dado(dado)
        return resul
