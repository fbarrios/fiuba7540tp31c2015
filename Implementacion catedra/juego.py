import interfaz_juego
import interfaz_jugador
import tablero
import jugador
import dados
import listado_cartas
import sys
import random

ARCHIVO_DEFAULT = "archivo.txt"
MINIMA_CANTIDAD_JUGADORES = 3
MIN_CARTAS_POR_JUGADOR = 5
LIBRE = "libre"


def obtener_de_archivo(archivo):
    linea = archivo.readline().rstrip()
    return linea.split(": ")[1].split(", ")


def cargar_datos(ruta):
    arch = open(ruta)
    casilleros = [casillero if casillero.lower() != LIBRE else None for casillero in obtener_de_archivo(arch)]
    personajes = obtener_de_archivo(arch)
    armas = obtener_de_archivo(arch)
    lugares = obtener_de_archivo(arch)
    arch.close()
    
    for lugar in lugares:
        if lugar not in casilleros:
            raise ValueError("lugares inaccesibles")
    return (personajes, armas, lugares), casilleros


def inicializacion(ruta, interfaz):
    cartas, casilleros = cargar_datos(ruta)
    tablero_juego = tablero.Tablero(casilleros)
    personajes, armas, lugares = cartas
    
    interfaz.set_personajes(personajes)
    interfaz.set_armas(armas)
    interfaz.set_lugares(lugares)
    
    total_cartas = len(personajes) + len(armas) + len(lugares)
    cant_jugadores = interfaz.pedir_cantidad_jugadores(MINIMA_CANTIDAD_JUGADORES, total_cartas / MIN_CARTAS_POR_JUGADOR)
    
    jugadores = []
    for i in range(cant_jugadores):
        listado = listado_cartas.ListadoCartas(personajes, armas, lugares)
        jugador_actual = jugador.Jugador(interfaz.pedir_nombre_jugador(i), 0, listado, dados.Dados(), interfaz) #por ahora los dados son los defaults
        jugadores.append(jugador_actual)
    
    return tablero_juego, jugadores, cartas


def jugar(tablero, jugadores, cartas_secretas, interfaz):   
    interfaz.dibujar_tablero(tablero)
    perdedores = []
    while True:
        if len(jugadores) == len(perdedores):
            return None
            
        jugador_toca = jugadores.pop(0)
        if jugador_toca in perdedores:
            jugadores.append(jugador_toca)
            continue
        
        interfaz.le_toca_a(jugador_toca)
        jugador_toca.mover(tablero)
        interfaz.dibujar_tablero(tablero)
        jugador_toca.sugerir(tablero, jugadores)
        
        intento = jugador_toca.jugarsela()
        if intento is not None:
            if intento == cartas_secretas:
                return jugador_toca
            else:
                interfaz.mostrar_perdedor(jugador_toca)
                perdedores.append(jugador_toca)
        jugadores.append(jugador_toca)


def clue(ruta):
    ijuego = interfaz_juego.Interfaz_Juego()
    ijugador = interfaz_jugador.Interfaz_Jugador()
    tablero, jugadores, cartas = inicializacion(ruta, ijugador)
    
    for jugador in jugadores:
		ijuego.agregar_jugador(jugador)
    
    personajes, armas, lugares = cartas
    secretas = (random.choice(personajes), random.choice(armas), random.choice(lugares))
    personajes.remove(secretas[0])
    armas.remove(secretas[1])
    lugares.remove(secretas[2])
    
    cartas_restantes = personajes + armas + lugares
    random.shuffle(cartas_restantes)
    
    i = 0
    while len(cartas_restantes) > 0:
        jugadores[i].asignar_carta(cartas_restantes.pop())
        i = (i + 1) % len(jugadores)
    print secretas
    
    ganador = jugar(tablero, jugadores, secretas, ijuego)
    if ganador is not None:
        interfaz_juego.mostrar_ganador(ganador)
    else:
        interfaz_juego.mostrar_sin_ganador()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        clue(ARCHIVO_DEFAULT)
    else:
        clue(sys.argv[1])
