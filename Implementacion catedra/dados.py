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
    def __init__(self, prob_dados = (DEFAULTS, DEFAULTS)):
        '''Recibe un iterable con las probabilidades de cada resultado del dado (empezando por 1).
        Parametros:
            - prob_dados: un iterable con tantos elementos como dados se quieran tener.
            Cada elemento de prob_dados debe ser un iterable, con tantos elementos como caras se deseen, con la probabilidad
            de aparicion de cada cara. La suma de las probabilidades debe ser 1, o muy similar, sino lanzara un ValueError.'''
        self.dados = prob_dados
        for dado in prob_dados:
            suma = 0
            for prob in dado:
                suma += prob
            if abs(suma - 1) > 0.05:
                raise ValueError('La suma de probabilidades de alguno de los dados no es 1')
        
    def lanzar(self):
        '''Lanza todos los dados que tiene, con sus probabilidades asignadas, y
        devuelve la suma de todos los resultados de lanzadas'''
        resul = 0
        for dado in self.dados:
            resul += resultado_dado(dado)
        return resul
