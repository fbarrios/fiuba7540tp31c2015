import dados
import random
import tablero
import pygame
import sys
from pygame.locals import *

FIN_COLOR = '\033[0m'
COLORES = 1
JUGADOR = 0
COLOR_PANTALLA = 0
COLOR_SHELL = 1

ANCHO_PANTALLA = 660
ALTO_PANTALLA = 510
FONDO_PANTALLA = 'imagenes/board.png'
pygame.init()

VER_POSIBILIDADES = "*"
DADO_ESTADAR = "*"


def pedir_numero(minimo, maximo, mensaje):
    """Obtiene un numero del usuario, entre los valores minimos y maximos."""
    while True:
        valor = raw_input(mensaje)
        if not valor.isdigit():
            print "Error, debe ingresar un valor numerico"
            continue
        valor = int(valor)
        if minimo <= valor <= maximo:
            return valor
        else:
            print "Error, debe ingresar un valor entre", minimo, "y", maximo


def pedir_carta(posibilidades, tipo):
    """Le pide al usuario que elija alguna de todas las posibilidades de cartas, de un determinado tipo"""
    while True:
        valor = raw_input("Ingrese " + tipo + ". Si quiere ver todas las posibilidades, ingrese " + VER_POSIBILIDADES + "\n")
        if valor in posibilidades:
            return valor
        elif valor == VER_POSIBILIDADES:
            for carta in posibilidades:
                print "-", carta
        else:
            print "Error, ingrese un " + tipo + " valida"


def pregunta_si_no(pregunta):
    pregunta += " S/N\n"
    while True:
        si_no = raw_input(pregunta)
        if si_no.upper() == "S": return True
        elif si_no.upper() == "N": return False
        else: print "Error"


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
        return pedir_numero(minimo, maximo, "Ingrese la cantidad de jugadores, entre " + str(minimo) + " y " + str(maximo) + ":\n")

    def pedir_nombre_jugador(self, num_jugador):
        """Le pide al usuario el nombre de un jugador. No se permite ingresar un nombre que ya fuere ingresado"""
        while True:
            nombre = raw_input("Ingrese nombre del jugador " + str(num_jugador + 1) + ":\n")
            if nombre in self.nombres:
                print "Error, ya fue ingresado ese nombre"
                continue
            self.nombres.append(nombre)
            return nombre

    def pedir_dados(self, jugador, max_dados, max_caras_dados):
        """Obtiene los dados del que debera tener el jugador indicado."""
        cantidad = pedir_numero(1, max_dados, "Ingrese la cantidad de dados que tendra el jugador " + jugador + "\n")
        dices = []
        for i in range(cantidad):
            caras = pedir_numero(1, max_caras_dados, "Ingrese la cantidad de caras que tendra el dado " + str(i+1) + "\n")
            print "Que tipo de dado es?"
            print "1) Estandar (todas las caras equiprobables)"
            print "2) Creciente"
            print "3) Decreciente"
            print "4) Triangular"
            tipo_dado = pedir_numero(1, len(dados.GENERADORES), "Ingrese opcion valida de dado\n")
            generado = dados.GENERADORES[tipo_dado - 1](caras)
            dices.append(generado)
        return dices

    def pedir_carta_a_mostrar(self, jugador, posibles):
        """Le pide al jugador que elija entre todas las cartas posibles, para mostrarselas a otro jugador."""
        print jugador.get_nombre(), "Debe elegir entre:"
        for i in range(len(posibles)):
            print str(i + 1) + ")" ,posibles[i]
        return posibles[pedir_numero(1, len(posibles), "Ingrese una opcion valida\n") - 1]

    def pedir_sentido(self):
        """Le pide el sentido al usuario. Se devuelven los valores de las constantes indicadas en el tablero."""
        print "Deseas moverte en sentido horario o sentido antihorario?"
        print "1) Horario"
        print "2) Antirhorario"
        if (pedir_numero(1,2, "Ingrese una opcion valida\n") == 1):
            return tablero.HORARIO
        else:
            return tablero.ANTIHORARIO

    def quiere_consultar(self, lugar):
        """Le pregunta al usuario si desea realizar una sugerencia o no. Devuelve un valor Booleano con la respuesta"""
        return pregunta_si_no("Quiere hacer una sugerencia en " + lugar + "?")

    def pedir_personaje(self):
        """Le pide al usuario un personaje."""
        return pedir_carta(self.personajes, "Personaje")

    def pedir_arma(self):
        """Le pide al usuario un arma"""
        return pedir_carta(self.armas, "Arma")

    def pedir_lugar(self):
        """Le pide al usuario un lugar"""
        return pedir_carta(self.lugares, "Lugar")

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
        for carta in mano:
            print carta + ",",
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
        for tirada in resultados:
            print str(tirada) + ",",
        print "Total:", sum(resultados)


class InterfazJuego(object):
    """Abstrae la interfaz del juego. Permite pedirle cosas a un usuario sobre el juego, y a su vez permite 
    cambiar la forma en las que esto se hace."""
    def __init__(self):
        self.jugadores = []
        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        pygame.display.set_caption("Clue!")
        self.background_image = pygame.image.load(FONDO_PANTALLA)
        COLORES_PANTALLA = [(pygame.image.load('imagenes/greenplayer.png').convert_alpha(), '\033[92m'),
                            (pygame.image.load('imagenes/blueplayer.png').convert_alpha(), '\033[94m'),
                            (pygame.image.load('imagenes/redplayer.png').convert_alpha(), '\033[91m'),
                            (pygame.image.load('imagenes/yellowplayer.png').convert_alpha(), '\033[93m'),
                            (pygame.image.load('imagenes/pinkplayer.png').convert_alpha(),'\033[95m'),
                            (pygame.image.load('imagenes/greyplayer.png').convert_alpha(), '\033[90m')]
        self.colores = COLORES_PANTALLA[:]
      
    def agregar_jugador(self, jugador):
        """Se agrega un jugador, y se le asigna un color de forma aleatoria"""
        color = random.choice(self.colores)
        self.colores.remove(color)
        self.jugadores.append((jugador, color))
    
    def dibujar_tablero(self, tablero):
        """Dibuja el tablero, con los jugadores (solo el primero de todos los que ocupen la misma posicion)"""
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        self.pantalla.blit(self.background_image, (0, 0))
        for jugador_color in self.jugadores[::-1]:
            posicion = jugador_color[JUGADOR].get_posicion()
            self.pantalla.blit(jugador_color[COLORES][COLOR_PANTALLA], tablero.posicion_de_casillero(posicion))
        pygame.display.flip()
    
    def color_de_jugador(self, jugador):
        """Metodo auxiliar que busca el par <jugador, color>"""
        for jugador_color in self.jugadores:
            if jugador_color[JUGADOR] == jugador:
                return jugador_color[COLORES]
                
    def mostrar_perdedor(self, jugador):
        """Muestra a un jugador perdedor, y no lo vuelve a mostrar mas en el tablero (aunque siga siendo parte del juego)"""
        color = self.color_de_jugador(jugador)
        print color[COLOR_SHELL], jugador.get_nombre(),FIN_COLOR, "ha perdido! Suerte para la proxima"
        self.jugadores.remove((jugador, color))
    
    def mostrar_ganador(self, jugador):
        """Muestra al jugador ganador"""
        print self.color_de_jugador(jugador)[COLOR_SHELL], jugador.get_nombre(), "HA GANADO!!!!!", FIN_COLOR
        
    def le_toca_a(self, jugador):
        """Muestra que le toca a un jugador, con su color correspondiente."""
        print "Es el turno de", self.color_de_jugador(jugador)[COLOR_SHELL], jugador.get_nombre(), FIN_COLOR
       
    def mostrar_sin_ganador(self):
        """Muestra que no hubo ningun ganador."""
        print "Todos perdieron!!! que malos detectives que son!"
