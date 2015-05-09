import random
STADARD = (1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6)

def dado_standard(cant_caras):
    '''Devuelve una lista con las probabilidades de cada cara de un dado estandard (todas las caras equiprobables)'''
    return [1.0 / cant_caras for i in range(cant_caras)]

def dado_creciente(cant_caras):
    '''Devuelve una lista con las probabilidades de cada cara de un dado en el cual las caras de mayor numero tienen mayor probabilidad
    (probabilidad creciente).'''
    suma = cant_caras * (cant_caras + 1) / 2
    return [ (i + 1) * 1.0 / suma for i in range(cant_caras)]

def dado_decreciente(cant_caras):
    '''Devuelve una lista con las probabilidades de cada cara de un dado en el cual las caras de menor numero tienen mayor probabilidad
    (probabilidad decreciente).'''
    return dado_creciente(cant_caras)[::-1]

def dado_triangular(cant_caras):
    '''Devuelve una lista con las probabilidades de cada cara de un dado en el cual las caras cercanas al valor medio tienen mayor probabilidad,
    y a medida que me voy alejando del valor medio, la probabilidad va decreciendo (probabilidad triangular).'''
    media = (cant_caras + 1) / 2
    suma = cant_caras * (cant_caras + 1) / 2
    triangulo = [(suma - abs(i - media)) for i in range(cant_caras)]
    triangulo_normalizado = [ 1.0 * elemento / sum(triangulo) for elemento in triangulo]
    return triangulo_normalizado
    
    
def resultado_dado(probabilidades):
    u = random.random()
    value = 0
    prob_acum = 0
    while u > prob_acum:
        prob_acum += probabilidades[value]
        value += 1
    return value

GENERADORES = [dado_standard, dado_creciente, dado_decreciente, dado_triangular]

class Dados(object):
    '''Representa un conjunto de dados que, dadas la cantidad de caras y probabilidades de cada uno de estas, permite lanzarlos.'''
    def __init__(self, prob_dados = (STADARD, STADARD)):
        '''Recibe un iterable con las probabilidades de cada resultado del dado (empezando por 1).
        Parametros:
            - prob_dados: un iterable con tantos elementos como dados se quieran tener.
            Cada elemento de prob_dados debe ser un iterable, con tantos elementos como caras se deseen, con la probabilidad
            de aparicion de cada cara. La suma de las probabilidades debe ser 1, o muy similar, sino lanzara un ValueError.'''
        self.dados = prob_dados
        for dado in prob_dados:
            suma = sum(dado)
            if abs(suma - 1) > 0.05:
                raise ValueError('La suma de probabilidades de alguno de los dados no es 1')
        
    def lanzar(self):
        '''Lanza todos los dados que tiene, con sus probabilidades asignadas, y
        devuelve la suma de todos los resultados de lanzadas'''
        resul = 0
        for dado in self.dados:
            resul += resultado_dado(dado)
        return resul
