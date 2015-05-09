import random
import tablero
COLORES = ['\033[95m', '\033[94m', '\033[93m', '\033[92m', '\033[91m', '\033[90m']

FIN_COLOR = '\033[0m'
COLOR = 1
JUGADOR = 0

class InterfazJuego(object):
    def __init__(self):
        self.jugadores = []
        self.colores = COLORES[:]
      
    def agregar_jugador(self, jugador):
        '''Se agrega un jugador, y se le asigna un color de forma aleatoria'''
        color = random.choice(self.colores)
        self.colores.remove(color)
        self.jugadores.append((jugador, color))
    
    def dibujar_tablero(self, tablero):
        '''Dibuja el tablero, con los jugadores (solo el primero de todos los que ocupen la misma posicion)'''
        casilleros_ocupados = {}
        for jugador_color in self.jugadores:
            posicion = jugador_color[JUGADOR].get_posicion()
            if posicion not in casilleros_ocupados:
                casilleros_ocupados[posicion] = []
            casilleros_ocupados[posicion].append(jugador_color)
        
        print "--------------------------"
        cadena_casilleros = []
        for casillero in range(len(tablero)):
            cadena = ""
            if casillero in casilleros_ocupados:
                cadena = casilleros_ocupados[casillero][0][COLOR] + casilleros_ocupados[casillero][0][JUGADOR].get_nombre() + FIN_COLOR
            else:
                if tablero[casillero] is not None:
                    cadena = tablero[casillero]
                else:
                    cadena = "[]"
            cadena_casilleros.append(cadena)
        print "|".join(cadena_casilleros)
        print "--------------------------"
    
    def color_de_jugador(self, jugador):
        '''Metodo auxiliar que busca el par <jugador, color>'''
        for jugador_color in self.jugadores:
            if jugador_color[JUGADOR] == jugador:
                return jugador_color
                
    def mostrar_perdedor(self, jugador):
        '''Muestra a un jugador perdedor, y no lo vuelve a mostrar mas en el tablero (aunque siga siendo parte del juego)'''
        print self.color_de_jugador(jugador)[COLOR], jugador.get_nombre(),FIN_COLOR, "ha perdido! Suerte para la proxima"
        self.jugadores.remove(self.color_de_jugador(jugador))
    
    def mostrar_ganador(self, jugador):
        '''Muestra al jugador ganador'''
        print self.color_de_jugador(jugador)[COLOR], jugador.get_nombre(), "HA GANADO!!!!!", FIN_COLOR
        
    def le_toca_a(self, jugador):
        '''Muestra que le toca a un jugador, con su color correspondiente.'''
        print "Es el turno de",self.color_de_jugador(jugador)[COLOR],jugador.get_nombre(),FIN_COLOR
       
    def mostrar_sin_ganador(self):
        '''Muestra que no hubo ningun ganador.'''
        print "Todos perdieron!!! que malos detectives que son!"
