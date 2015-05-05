import random
import tablero

class Jugador(object):
    def __init__(self, nombre, posicion_inicial, listado_inicial, dados, interfaz):
        self.posicion = posicion_inicial
        self.listado = listado_inicial
        self.mano = []
        self.dados = dados
        self.interfaz = interfaz
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre
        
    def __eq___(self, otro):
        return self.nombre == otro.nombre
    
    def asignar_carta(self, carta):
        self.mano.append(carta)
        self.listado.sacar_carta(carta)
    
    def __hash__(self):
        return __hash__(self.nombre)
    
    def get_posicion(self):
        return self.posicion
    
    def get_mano(self): #ver si esto lo hacemos de otra manera
        return self.mano
    
    def alguna_carta(self, jugada):
        eleccion = []
        for carta in jugada:
            if carta in self.mano:
                eleccion.append(carta)
        if len(eleccion) == 0:
            return None
        else:
            return self.interfaz.pedir_carta_a_mostrar(self, eleccion)
    
    def jugarsela(self):
        se_la_juega = self.interfaz.preguntar_arriesgo()
        return se_la_juega
    
    def mover(self, tablero):       
        lanzado = self.dados.lanzar()
        self.interfaz.mostrar_dados(lanzado)
        horario = self.interfaz.pedir_sentido()
        self.posicion = tablero.siguiente(self.posicion, lanzado, horario)
    
    def sugerir(self, tablero, otros_jugadores):
        lugar = tablero[self.posicion]
        if lugar is None or not self.interfaz.quiere_consultar(lugar):
            return
        self.interfaz.mostrar_mano(self.get_mano())
        self.interfaz.mostrar_listado(self.get_listado_str())
        
        personaje = self.interfaz.pedir_personaje()
        arma = self.interfaz.pedir_arma()
        
        for jugador in otros_jugadores:
            carta = jugador.alguna_carta( (personaje, arma, lugar) )
            if carta is not None:
                self.interfaz.mostrar_carta(jugador, carta)
                self.listado.sacar_carta(carta)
                return
        self.interfaz.mostrar_no_hay_cartas()
        
    def get_listado_str(self):
        return str(self.listado)

