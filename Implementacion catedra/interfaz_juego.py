import random
import tablero
import pygame
from pygame.locals import *

FIN_COLOR = '\033[0m'
COLORES = 1
JUGADOR = 0
COLOR_PANTALLA = 0
COLOR_SHELL = 1

ANCHO_PANTALLA = 660
ALTO_PANTALLA = 510
FONDO_PANTALLA = 'imagenes/board3.png'
pygame.init()

def load_image(filename, transparent=False):
    try: image = pygame.image.load(filename)
    except pygame.error, message:
            raise SystemExit, message
    image = image.convert()
    if transparent:
            color = image.get_at((0,0))
            image.set_colorkey(color, RLEACCEL)
    return image

class InterfazJuego(object):
    '''Abstrae la interfaz del juego. Permite pedirle cosas a un usuario sobre el juego, y a su vez permite 
    cambiar la forma en las que esto se hace.'''
    def __init__(self):
        self.jugadores = []
        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        pygame.display.set_caption("Clue!")
        self.background_image = load_image(FONDO_PANTALLA)
        COLORES_PANTALLA = [(load_image('imagenes/greenplayer.png'), '\033[92m'), (load_image('imagenes/blueplayer.png'), '\033[94m'), (load_image('imagenes/redplayer.png'), '\033[91m'), (load_image('imagenes/yellowplayer.png'), '\033[93m'), (load_image('imagenes/pinkplayer.png'),'\033[95m'), (load_image('imagenes/greyplayer.png'), '\033[90m')]
        self.colores = COLORES_PANTALLA
      
    def agregar_jugador(self, jugador):
        '''Se agrega un jugador, y se le asigna un color de forma aleatoria'''
        color = random.choice(self.colores)
        self.colores.remove(color)
        self.jugadores.append((jugador, color))
    
    def dibujar_tablero(self, tablero):
        '''Dibuja el tablero, con los jugadores (solo el primero de todos los que ocupen la misma posicion)'''
        self.pantalla.blit(self.background_image, (0, 0))
        for jugador_color in self.jugadores:
            posicion = jugador_color[JUGADOR].get_posicion()
            self.pantalla.blit(jugador_color[COLORES][COLOR_PANTALLA], tablero.posicion_de_casillero(posicion))
        pygame.display.flip()
    
    def color_de_jugador(self, jugador):
        '''Metodo auxiliar que busca el par <jugador, color>'''
        for jugador_color in self.jugadores:
            if jugador_color[JUGADOR] == jugador:
                return jugador_color[COLORES]
                
    def mostrar_perdedor(self, jugador):
        '''Muestra a un jugador perdedor, y no lo vuelve a mostrar mas en el tablero (aunque siga siendo parte del juego)'''
        color = self.color_de_jugador(jugador)
        print color[COLOR_SHELL], jugador.get_nombre(),FIN_COLOR, "ha perdido! Suerte para la proxima"
        self.jugadores.remove((jugador, color))
    
    def mostrar_ganador(self, jugador):
        '''Muestra al jugador ganador'''
        print self.color_de_jugador(jugador)[COLOR_SHELL], jugador.get_nombre(), "HA GANADO!!!!!", FIN_COLOR
        
    def le_toca_a(self, jugador):
        '''Muestra que le toca a un jugador, con su color correspondiente.'''
        print "Es el turno de",self.color_de_jugador(jugador)[COLOR_SHELL],jugador.get_nombre(),FIN_COLOR
       
    def mostrar_sin_ganador(self):
        '''Muestra que no hubo ningun ganador.'''
        print "Todos perdieron!!! que malos detectives que son!"
