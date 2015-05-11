import interfaces
import tablero
import jugador
import listado_cartas
import sys
import random

ARCHIVO_DEFAULT = "configuraciones.txt"
MINIMA_CANTIDAD_JUGADORES = 3
MIN_CARTAS_POR_JUGADOR = 5
LIBRE = "libre"
MAX_DADOS = 5
MAX_CARAS = 10


def obtener_de_archivo(archivo):
    """Obtiene una lista con todos los parametros indicados en la siguiente linea del archivo."""
    linea = archivo.readline().rstrip()
    return linea.split(": ")[1].split(", ")


def cargar_datos(ruta):
    """Obtiene las configuraciones del archivo de configuracion del tablero y cartas.
    Parametros:
        - ruta: ruta del archivo.
    Salida: tupla con las cartas (una tupla (personajes, armas, lugares)),  una lista de casilleros y
    una lista con posiciones (para visualizar en el tablero)."""
    arch = open(ruta)
    casilleros = [casillero if casillero.lower() != LIBRE else None for casillero in obtener_de_archivo(arch)]
    posiciones = [(int(pos.split("-")[0]), int(pos.split("-")[1])) for pos in obtener_de_archivo(arch)]
    personajes = obtener_de_archivo(arch)
    armas = obtener_de_archivo(arch)
    lugares = obtener_de_archivo(arch)
    arch.close()
    
    for lugar in lugares:
        if lugar not in casilleros:
            raise ValueError("lugares inaccesibles")
    return (personajes, armas, lugares), casilleros, posiciones


def inicializar_juego(ruta, interfaz):
    """Inicializa el juego, creando el tablero, cargando las cartas, cargando los nuevos jugadores."""
    cartas, casilleros, posiciones = cargar_datos(ruta)
    tablero_juego = tablero.Tablero(casilleros, posiciones)
    personajes, armas, lugares = cartas
    
    interfaz.set_personajes(personajes)
    interfaz.set_armas(armas)
    interfaz.set_lugares(lugares)
    
    total_cartas = len(personajes) + len(armas) + len(lugares)
    cant_jugadores = interfaz.pedir_cantidad_jugadores(MINIMA_CANTIDAD_JUGADORES, total_cartas / MIN_CARTAS_POR_JUGADOR)
    
    jugadores = []
    for i in range(cant_jugadores):
        listado = listado_cartas.ListadoCartas(personajes, armas, lugares)
        nombre = interfaz.pedir_nombre_jugador(i)
        jugador_actual = jugador.Jugador(nombre, 0, listado, interfaz.pedir_dados(nombre, MAX_DADOS, MAX_CARAS), interfaz)
        jugadores.append(jugador_actual)
    
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
        jugadores.append(jugador_turno)


def clue(ruta):
    """Carga las configuraciones desde la ruta dada, crea el tablero, cartas y jugadores, luego
    selecciona las cartas secretas, mezcla y asigna el resto a los jugadores. Empieza el juego, 
    y al terminar avisa si hubo ganador o todos perdieron."""
    interfaz_juego = interfaces.InterfazJuego()
    interfaz_jugador = interfaces.InterfazJugador()

    try:
        tablero, jugadores, cartas = inicializar_juego(ruta, interfaz_jugador)
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
    if len(sys.argv) == 1:
        clue(ARCHIVO_DEFAULT)
    else:
        clue(sys.argv[1])
