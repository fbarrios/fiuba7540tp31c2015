import random
import tablero
COLORES = ['\033[95m', '\033[94m', '\033[93m', '\033[92m', '\033[91m', '\033[90m']

FIN_COLOR = '\033[0m'

class Interfaz_Juego(object):
    def __init__(self):
        self.jugadores = []
        self.colores = COLORES[:]
      
    def agregar_jugador(self, jugador):
        color = random.choice(self.colores)
        self.colores.remove(color)
        self.jugadores.append((jugador, color))
    
    def dibujar_tablero(self, tablero):
        casilleros_ocupados = {}
        for jugador_color in self.jugadores:
            posicion = jugador_color[0].get_posicion()
            if posicion not in casilleros_ocupados:
                casilleros_ocupados[posicion] = []
            casilleros_ocupados[posicion].append(jugador_color)
        
        print "--------------------------"
        for casillero in range(len(tablero)):
            if casillero in casilleros_ocupados:
                print casilleros_ocupados[casillero][0][1] + casilleros_ocupados[casillero][0][0].get_nombre() + FIN_COLOR, #solo imprimo uno de ellos por ahora
            else:
                if tablero[casillero] is not None:
                    print tablero[casillero],
                else:
                    print "[]",
        print
        print "--------------------------"
        
    def mostrar_perdedor(self, jugador):
        print jugador.get_nombre(), "ha perdido! Suerte para la proxima"
        for jugador_color in self.jugadores:
            if jugador_color[0] == jugador:
                self.jugadores.remove(jugador_color)
                return
    
    def mostrar_ganador(self, jugador):
        print jugador.get_nombre(), "HA GANADO!!!!!"
        
    def le_toca_a(self, jugador):
        for jugador_color in self.jugadores:
            if jugador_color[0] == jugador:
                print "Es el turno de",jugador_color[1],jugador.get_nombre(),FIN_COLOR
       
    def mostrar_sin_ganador(self):
        print "Todos perdieron!!! que malos detectives que son!"
