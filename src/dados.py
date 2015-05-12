import random
ESTANDAR = (1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6)

TIPO_DADO_ESTANDAR = "Estandar (todas las caras equiprobables)"
TIPO_DADO_CRECIENTE = "Creciente"
TIPO_DADO_DECRECIENTE = "Decreciente"
TIPO_DADO_TRIANGULAR = "Triangular"
TIPOS_DADOS = [TIPO_DADO_ESTANDAR, TIPO_DADO_CRECIENTE, TIPO_DADO_DECRECIENTE, TIPO_DADO_TRIANGULAR]


class Dado(object):
    """Clase que representa un dado para obtener un numero aletorio,
    con una distribucion de probabilidades dada por cada cara."""

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

    def obtener_probabilidades(self):
        return self.probabilidades[:]
        
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


class DadoEstandar(Dado):
    """Clase que representa un dado con una distribucion de probabilidades estandar."""
    def __init__(self, caras):
        Dado.__init__(self, [1.0 / caras for i in range(caras)])


class DadoCreciente(Dado):
    """Clase que representa un dado con una distribucion de probabilidades creciente."""
    def __init__(self, caras):
        suma = caras * (caras + 1) / 2
        Dado.__init__(self, [ (i + 1) * 1.0 / suma for i in range(caras)])


class DadoDecreciente(Dado):
    """Clase que representa un dado con una distribucion de probabilidades decreciente."""
    def __init__(self, caras):
        suma = caras * (caras + 1) / 2
        Dado.__init__(self, [ (i + 1) * 1.0 / suma for i in range(caras)][::-1])


class DadoTriangular(Dado):
    """Clase que representa un dado con una distribucion de probabilidades triangular:
    las caras cercanas al valor medio tienen mayor probabilidad, y a medida que nos alejamos
    de dicho valor la probabilidad va disminuyendo."""
    def __init__(self, caras):
        media = (caras + 1) / 2
        suma = caras * (caras + 1) / 2
        triangulo = [(suma - abs(i - media)) for i in range(caras)]
        triangulo_normalizado = [ 1.0 * elemento / sum(triangulo) for elemento in triangulo]
        Dado.__init__(self, triangulo_normalizado)
        

GENERADORES = [DadoEstandar, DadoCreciente, DadoDecreciente, DadoTriangular]
