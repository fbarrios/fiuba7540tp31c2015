import dados
import tablero
from entrada_usuario import *


class InterfazJugador(object):
    """Abstae la interfaz hacia el usuario, para solicitarle ingresos respecto a un determinado
    jugador, manejado por dicho usuario."""
    def __init__(self):
        self.armas = []
        self.lugares = []
        self.personajes = []
        self.nombres = []

    def set_personajes(self, personajes):
        """Se le asignan los personajes del juego"""
        self.personajes = personajes[:]

    def set_armas(self, armas):
        """Se le asignan las armas del juego"""
        self.armas = armas[:]

    def set_lugares(self, lugares):
        """Se le asignan los lugares del juego"""
        self.lugares = lugares[:]

    def pedir_cantidad_jugadores(self, minimo, maximo):
        """Le pide al usuario la cantidad de jugadores que van a jugar"""
        return solicitar_numero(minimo, maximo, "Ingrese la cantidad de jugadores, entre " + str(minimo) + " y " + str(maximo) + ":\n")

    def pedir_nombre_jugador(self, num_jugador):
        """Le pide al usuario el nombre de un jugador. No se permite ingresar un nombre que ya fuere ingresado"""
        return solicitar_nombre_jugador(self.nombres, num_jugador)

    def pedir_dados(self, jugador, max_dados, max_caras_dados):
        """Obtiene los dados del que debera tener el jugador indicado."""
        cantidad = solicitar_numero(1, max_dados, "Ingrese la cantidad de dados que tendra el jugador " + jugador + ".\n")
        dados_jugadores = []
        for i in range(cantidad):
            caras = solicitar_numero(1, max_caras_dados, "Ingrese la cantidad de caras que tendra el dado " + str(i+1) + ".\n")
            print "Tipos de dados disponibles:"
            mostrar_posibilidades(dados.TIPOS_DADOS)
            tipo_dado = solicitar_entre_opciones(dados.TIPOS_DADOS, "que tipo de dado desea usar")
            generado = dados.GENERADORES[tipo_dado](caras)
            dados_jugadores.append(generado)
        return dados_jugadores

    def pedir_carta_a_mostrar(self, jugador, posibles):
        """Le pide al jugador que elija entre todas las cartas posibles, para mostrarselas a otro jugador."""
        print jugador.get_nombre(), "debe elegir entre:"
        mostrar_posibilidades(posibles)
        indice_carta = solicitar_entre_opciones(posibles, "la carta a mostrar")
        return posibles[indice_carta]

    def pedir_sentido(self):
        """Le pide el sentido al usuario. Se devuelven los valores de las constantes indicadas en el tablero."""
        print "Deseas moverte en sentido horario o sentido antihorario?"
        mostrar_posibilidades(tablero.SENTIDOS)
        indice_sentido = solicitar_entre_opciones(tablero.SENTIDOS, "el sentido del movimiento")
        if tablero.SENTIDOS[indice_sentido] == tablero.SENTIDO_HORARIO:
            return tablero.HORARIO
        else:
            return tablero.ANTIHORARIO

    def quiere_consultar(self, lugar):
        """Le pregunta al usuario si desea realizar una sugerencia o no. Devuelve un valor Booleano con la respuesta"""
        return pregunta_si_no("Quiere hacer una sugerencia en " + lugar + "?")

    def pedir_personaje(self):
        """Le pide al usuario un personaje."""
        indice_personaje = solicitar_entre_opciones(self.personajes, "Personaje")
        return self.personajes[indice_personaje]

    def pedir_arma(self):
        """Le pide al usuario un arma"""
        indice_arma = solicitar_entre_opciones(self.armas, "Arma")
        return self.armas[indice_arma]

    def pedir_lugar(self):
        """Le pide al usuario un lugar"""
        indice_lugar = solicitar_entre_opciones(self.lugares, "Lugar")
        return self.lugares[indice_lugar]

    def mostrar_carta(self, jugador, carta):
        """Le muestra al jugador que realizo la sugerencia la carta que el jugador (recibido por parametro) le
        muestra para afirmar que su sugerencia es falsa."""
        print "Tu sugerencia no es cierta!", jugador.get_nombre(), "tenia la carta", carta

    def mostrar_no_hay_cartas(self):
        """Le avisa al jugador que realizo la sugerenca que ningun otro jugador puede presentar pruebas
        para afirmarla falsa."""
        print "Ninguna de las cartas pedidas la tiene otro jugador! que sospechoso!"

    def preguntar_arriesgo(self):
        """Le consulta al usuario si desea arriesgar. En caso afirmativo le pide las cartas del arriesgo y devuelve
        una tupla (personaje, arma, lugar),    en caso negativo devuelve None"""
        rta = pregunta_si_no("Desea arriesgarse?")
        if not rta:
            return None
        personaje = self.pedir_personaje()
        arma = self.pedir_arma()
        lugar = self.pedir_lugar()
        return personaje, arma, lugar

    def mostrar_mano(self, mano):
        """Muestra la mano de un jugador"""
        print "Tu mano es:"
        print ", ".join(mano)
        print

    def mostrar_listado(self, listado):
        """Muestra el listado de cartas que aun no vio un determinado jugador"""
        print "Las cartas que aun no viste son:"
        print listado

    def mostrar_dados(self, resultados):
        """Le muestra al usuario el resultado de la lanzada de dados.
        Parametros:
            - resultados: un iterable con los resultados del lanzamiento de cada dado"""
        print "Tiraste un....",
        print ", ".join([str(resultado) for resultado in resultados])
        print "Total:", sum(resultados)
