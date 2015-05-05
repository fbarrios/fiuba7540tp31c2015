import tablero

def pedir_numero(minimo, maximo, mensaje):
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
    while True:
        valor = raw_input("Ingrese " + tipo + "\n")
        if valor in posibilidades:
            return valor
        print "Error, ingrese un " + tipo + " valida"



class Interfaz_Jugador(object):
    def __init__(self):
        self.armas = []
        self.lugares = []
        self.personajes = []
    
    def set_personajes(self, personajes):
        self.personajes = personajes[:]
    
    def set_armas(self, armas):
        self.armas = armas[:]
    
    def set_lugares(self, lugares):
        self.lugares = lugares[:]

    def pedir_cantidad_jugadores(self, minimo, maximo):
        return pedir_numero(minimo, maximo, "Ingrese la cantidad de jugadores:\n") 
        
    def pedir_nombre_jugador(self, num_jugador):
        return raw_input("Ingrese nombre del jugador " + str(num_jugador + 1) + ":\n")
        
    def pedir_carta_a_mostrar(self, jugador, posibles):
        print jugador.get_nombre(), "Debe elegir entre:"
        for i in range(len(posibles)):
            print i+1, ")" ,posibles[i]
        return posibles[pedir_numero(1, len(posibles), "Ingrese una opcion valida\n") - 1]

    def pedir_sentido(self):
        #no valido porque ya fue:
        while True: 
            sentido = raw_input("Sentido horario o antihorario?\n")
            if sentido == "horario": return tablero.HORARIO
            elif sentido == "antihorario": return tablero.ANTIHORARIO
            else: print "Error, ingrese opcion valida"

    def quiere_consultar(self, lugar):
        while True:
            si_no = raw_input("Quiere hacer una sugerencia en " + lugar + "?S/N\n")
            if si_no.upper() == "S": return True
            elif si_no.upper() == "N": return False
            else: print "Error"
    
    def pedir_personaje(self):
        return pedir_carta(self.personajes, "Personaje")
            
    def pedir_arma(self):
        return pedir_carta(self.armas, "Arma")
    
    def pedir_lugar(self):
        return pedir_carta(self.lugares, "Lugar")

    def mostrar_carta(self, jugador, carta):
        print "Tu sugerencia no es cierta!", jugador.get_nombre(), "tenia la carta", carta
    
    def mostrar_no_hay_cartas(self):
        print "Ninguna de las cartas pedidas la tiene otro jugador! que sospechoso!"
        
    def preguntar_arriesgo(self):
        while True:
            si_no = raw_input("Desea arriesgarse? S/N\n")
            if si_no.upper() == "N": return None
            elif si_no.upper() == "S": break
            else: print "error"
            
        personaje = self.pedir_personaje()
        arma = self.pedir_arma()
        lugar = self.pedir_lugar()
        return personaje, arma, lugar
        
    def mostrar_mano(self, mano):
        print "Tu mano es:"
        for carta in mano:
            print carta,
        print
    
    def mostrar_listado(self, listado):
        print "Las cartas que aun no viste son:"
        print listado
    
    def mostrar_dados(self, resul):
        print "Tiraste un....", resul
