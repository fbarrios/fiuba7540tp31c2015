from interfaz_juego import InterfazJuego
from interfaz_jugador import InterfazJugador
from tablero import Tablero
from jugador import Jugador
from listado_cartas import ListadoCartas
import random

# Parametros del juego.
ARCHIVO_CASILLEROS = "datos/casilleros.txt"
ARCHIVO_POSICIONES = "datos/posiciones.txt"
ARCHIVO_PERSONAJES = "datos/personajes.txt"
ARCHIVO_ARMAS = "datos/armas.txt"
ARCHIVO_LUGARES = "datos/lugares.txt"

MINIMA_CANTIDAD_JUGADORES = 3
MIN_CARTAS_POR_JUGADOR = 5
LIBRE = "libre"
MAX_DADOS = 5
MAX_CARAS = 10


def obtener_datos(nombre_archivo):
    """Obtiene una lista con el contenido del archivo."""
    with open(nombre_archivo) as archivo:
        return [linea.rstrip() for linea in archivo]


def inicializar_juego(interfaz):
    """Inicializa el juego, creando el tablero, cargando las cartas, cargando los nuevos jugadores."""

    # Carga los datos de los archivos.
    casilleros = [casillero if casillero != LIBRE else None
                    for casillero in obtener_datos(ARCHIVO_CASILLEROS)]
    posiciones = [(int(posicion.split(',')[0]), int(posicion.split(',')[1]))
                    for posicion in obtener_datos(ARCHIVO_POSICIONES)]
    tablero_juego = Tablero(casilleros, posiciones)

    lugares = obtener_datos(ARCHIVO_LUGARES)
    personajes = obtener_datos(ARCHIVO_PERSONAJES)
    armas = obtener_datos(ARCHIVO_ARMAS)

    # Verifica que todos los lugares sean accesibles desde el tablero.
    for lugar in lugares:
        if lugar not in casilleros:
            raise ValueError("lugares inaccesibles")

    interfaz.set_personajes(personajes)
    interfaz.set_armas(armas)
    interfaz.set_lugares(lugares)
    
    total_cartas = len(personajes) + len(armas) + len(lugares)
    cant_jugadores = interfaz.pedir_cantidad_jugadores(MINIMA_CANTIDAD_JUGADORES, total_cartas / MIN_CARTAS_POR_JUGADOR)
    
    jugadores = []
    for i in range(cant_jugadores):
        listado = ListadoCartas(personajes, armas, lugares)
        nombre = interfaz.pedir_nombre_jugador(i)
        jugador_actual = Jugador(nombre, 0, listado, interfaz.pedir_dados(nombre, MAX_DADOS, MAX_CARAS), interfaz)
        jugadores.append(jugador_actual)

    cartas = (personajes, armas, lugares)
    return tablero_juego, jugadores, cartas


def jugar(tablero, jugadores, cartas_secretas, interfaz):
    """Loop principal del juego. Se juega hasta que alguien haya ganado, o TODOS hayan perdido.
    Parametros:
        - tablero: Tablero del juego.
        - Jugadores: lista de jugadores, ordenada segun vaya la ronda.
        - cartas_secretas: tupla con las cartas secretas con el formato (personaje, arma, lugar)
        - interfaz: interfaz del juego, para mostrarle el tablero al usuario, y a quien le va tocando o perdiendo.
    Salida: el jugador que ha ganado, o None si todos han perdido"""
    interfaz.dibujar_tablero(tablero)
    perdedores = []
    while True:
        if len(jugadores) == len(perdedores):
            return None
        
        # Se saca al jugador de la ronda temporalmente.    
        jugador_turno = jugadores.pop(0)
        if jugador_turno in perdedores:
            jugadores.append(jugador_turno)
            continue
        
        interfaz.mostrar_turno(jugador_turno)
        jugador_turno.mover(tablero)
        interfaz.dibujar_tablero(tablero)
        jugador_turno.sugerir(tablero, jugadores)
        
        intento = jugador_turno.arriesgar()
        if intento is not None:
            if intento == cartas_secretas:
                return jugador_turno
            else:
                interfaz.mostrar_perdedor(jugador_turno)
                perdedores.append(jugador_turno)

        # Se agrega al jugador al final de la cola.
        jugadores.append(jugador_turno)


def clue():
    """ Ejecuta el juego de Clue.
    Carga las configuraciones, crea el tablero, cartas y jugadores.
    Lugo selecciona las cartas secretas, mezcla y asigna el resto a los jugadores.
    Empieza el juego, y al terminar avisa si hubo ganador o todos perdieron."""
    interfaz_juego = InterfazJuego()
    interfaz_jugador = InterfazJugador()

    try:
        tablero, jugadores, cartas = inicializar_juego(interfaz_jugador)
    except IOError:
        raise IOError("El archivo de configuracion del tablero no existe!!")
    
    for jugador in jugadores:
        interfaz_juego.agregar_jugador(jugador)

    # Selecciona las cartas que van a ser secretas.
    personajes, armas, lugares = cartas
    secretas = (random.choice(personajes), random.choice(armas), random.choice(lugares))
    personajes.remove(secretas[0])
    armas.remove(secretas[1])
    lugares.remove(secretas[2])
    
    cartas_restantes = personajes + armas + lugares
    random.shuffle(cartas_restantes)

    # Asigna las cartas a los jugadores.
    i = 0
    while len(cartas_restantes) > 0:
        jugadores[i].asignar_carta(cartas_restantes.pop())
        i = (i + 1) % len(jugadores)
    
    ganador = jugar(tablero, jugadores, secretas, interfaz_juego)
    if ganador is not None:
        interfaz_juego.mostrar_ganador(ganador)
    else:
        interfaz_juego.mostrar_sin_ganador()


if __name__ == "__main__":
    clue()
