import random
ESTANDAR = (1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6)

TIPO_DADO_ESTANDAR = "Estandar (todas las caras equiprobables)"
TIPO_DADO_CRECIENTE = "Creciente"
TIPO_DADO_DECRECIENTE = "Decreciente"
TIPO_DADO_TRIANGULAR = "Triangular"
TIPOS_DADOS = [TIPO_DADO_ESTANDAR, TIPO_DADO_CRECIENTE, TIPO_DADO_DECRECIENTE, TIPO_DADO_TRIANGULAR]


class Dado(object):
    """Clase que representa un conjunto de dados que permiten obtener un numero aletorio, dadas la
    cantidad de caras y probabilidades de cada uno."""

    def __init__(self, prob_dados=ESTANDAR):
        """Recibe un iterable con las probabilidades de cada resultado del dado (empezando por 1).
        Parametros:
            - prob_dados: un iterable con tantos elementos como dados se quieran tener.
            Cada elemento de prob_dados debe ser un iterable, con tantos elementos como caras se deseen,
            con la probabilidad de aparicion de cada cara. La suma de las probabilidades debe ser 1 (o
            muy similar), sino lanzara una excepcion de tipo ValueError."""
        self.probabilidades = prob_dados[:]
        if abs(sum(self.probabilidades) - 1) > 0.05:
            raise ValueError('La suma de probabilidades de alguno de los dados no es 1')                
        
    def lanzar(self):
        """Lanza todos los dados que tiene, con sus probabilidades asignadas, y devuelve la suma de todos
        los resultados de lanzadas"""
        u = random.random()
        value = 0
        prob_acum = 0
        while u > prob_acum:
            prob_acum += self.probabilidades[value]
            value += 1
        return value


def dado_estandar(cant_caras):
    """Devuelve una lista con las probabilidades de cada cara de un dado estandar (todas las caras
    equiprobables)"""
    return Dado([1.0 / cant_caras for i in range(cant_caras)])


def dado_creciente(cant_caras):
    """Devuelve una lista con las probabilidades de cada cara de un dado en el cual las caras de mayor
    numero tienen mayor probabilidad (probabilidad creciente)."""
    suma = cant_caras * (cant_caras + 1) / 2
    return Dado([ (i + 1) * 1.0 / suma for i in range(cant_caras)])


def dado_decreciente(cant_caras):
    """Devuelve una lista con las probabilidades de cada cara de un dado en el cual las caras de menor
    numero tienen mayor probabilidad (probabilidad decreciente)."""
    dado = dado_creciente(cant_caras)
    return dado.probabilidades[::-1]


def dado_triangular(cant_caras):
    """Devuelve una lista con las probabilidades de cada cara de un dado en el cual las caras cercanas
    al valor medio tienen mayor probabilidad, y a medida que me voy alejando del valor medio, la
    probabilidad va decreciendo (probabilidad triangular)."""
    media = (cant_caras + 1) / 2
    suma = cant_caras * (cant_caras + 1) / 2
    triangulo = [(suma - abs(i - media)) for i in range(cant_caras)]
    triangulo_normalizado = [ 1.0 * elemento / sum(triangulo) for elemento in triangulo]
    return Dado(triangulo_normalizado)


GENERADORES = [dado_estandar, dado_creciente, dado_decreciente, dado_triangular]