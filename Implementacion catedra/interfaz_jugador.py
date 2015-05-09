import tablero
import dados

VER_POSIBILIDADES = "*"
DADO_ESTADAR = "*"

def pedir_numero(minimo, maximo, mensaje):
    '''Obtiene un numero del usuario, entre los valores minimos y maximos.'''
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
    '''Le pide al usuario que elija alguna de todas las posibilidades de cartas, de un determinado tipo'''
    while True:
        valor = raw_input("Ingrese " + tipo + ". Si quiere ver todas las posibilidades, ingrese " + VER_POSIBILIDADES + "\n")
        if valor in posibilidades:
            return valor
        elif valor == VER_POSIBILIDADES:
            for carta in posibilidades:
                print "-", carta
        else:
            print "Error, ingrese un " + tipo + " valida"

class InterfazJugador(object):
    '''Abstae la interfaz hacia el usuario, para pedirle cosas respecto a un determinado jugador, manejado por dicho usuario.'''
    def __init__(self):
        self.armas = []
        self.lugares = []
        self.personajes = []
    
    def set_personajes(self, personajes):
        '''Se le asignan los personajes del juego'''
        self.personajes = personajes[:]
    
    def set_armas(self, armas):
        '''Se le asignan las armas del juego'''
        self.armas = armas[:]
    
    def set_lugares(self, lugares):
        '''Se le asignan los lugares del juego'''
        self.lugares = lugares[:]

    def pedir_cantidad_jugadores(self, minimo, maximo):
        '''Le pide al usuario la cantidad de jugadores que van a jugar'''
        return pedir_numero(minimo, maximo, "Ingrese la cantidad de jugadores, entre " + str(minimo) + " y " + str(maximo) + ":\n") 
        
    def pedir_nombre_jugador(self, num_jugador):
        '''Le pide al usuario el nombre de un jugador'''
        return raw_input("Ingrese nombre del jugador " + str(num_jugador + 1) + ":\n")
    
    def pedir_dados(self, jugador, max_dados, max_caras_dados):
        '''Obtiene los dados del que debera tener el jugador indicado.'''
        cantidad = pedir_numero(1, max_dados, "Ingrese la cantidad de dados que tendra el jugador " + jugador + "\n")
        probabilidades = []
        for i in range(cantidad):
            caras = pedir_numero(1, max_caras_dados, "Ingrese la cantidad de caras que tendra el dado " + str(i+1) + "\n")
            print "Que tipo de dado es?"
            print "1) Estandar (todas las caras equiprobables)"
            print "2) Creciente lineal"
            print "3) Decreciente lineal"
            print "4) Triangular"
            tipo_dado = pedir_numero(1, len(dados.GENERADORES), "Ingrese opcion valida de dado\n")
            generado = dados.GENERADORES[tipo_dado - 1](caras)
            probabilidades.append(generado)
        return dados.Dados(probabilidades)
        
    def pedir_carta_a_mostrar(self, jugador, posibles):
        '''Le pide al jugador que elija entre todas las cartas posibles, para mostrarselas a otro jugador.'''
        print jugador.get_nombre(), "Debe elegir entre:"
        for i in range(len(posibles)):
            print str(i + 1) + ")" ,posibles[i]
        return posibles[pedir_numero(1, len(posibles), "Ingrese una opcion valida\n") - 1]

    def pedir_sentido(self):
        '''Le pide el sentido al usuario. Se devuelven los valores de las constantes indicadas en el tablero.'''
        print "Deseas moverte en sentido horario o sentido antihorario?"
        print "1) Horario"
        print "2) Antirhorario"
        if (pedir_numero(1,2, "Ingrese una opcion valida\n") == 1):
            return tablero.HORARIO
        else:
            return tablero.ANTIHORARIO

    def quiere_consultar(self, lugar):
        '''Le pregunta al usuario si desea realizar una sugerencia o no. Devuelve un valor Booleano con la respuesta'''
        while True:
            si_no = raw_input("Quiere hacer una sugerencia en " + lugar + "?S/N\n")
            if si_no.upper() == "S": return True
            elif si_no.upper() == "N": return False
            else: print "Error"
    
    def pedir_personaje(self):
        '''Le pide al usuario un personaje.'''
        return pedir_carta(self.personajes, "Personaje")
            
    def pedir_arma(self):
        '''Le pide al usuario un arma'''
        return pedir_carta(self.armas, "Arma")
    
    def pedir_lugar(self):
        '''Le pide al usuario un lugar'''
        return pedir_carta(self.lugares, "Lugar")

    def mostrar_carta(self, jugador, carta):
        '''Le muestra al jugador que realizo la sugerencia la carta que el jugador (recibido por parametro) le
        muestra para afirmar que su sugerencia es falsa.'''
        print "Tu sugerencia no es cierta!", jugador.get_nombre(), "tenia la carta", carta
    
    def mostrar_no_hay_cartas(self):
        '''Le avisa al jugador que realizo la sugerenca que ningun otro jugador puede presentar pruebas
        para afirmarla falsa.'''
        print "Ninguna de las cartas pedidas la tiene otro jugador! que sospechoso!"
        
    def preguntar_arriesgo(self):
        '''Le consulta al usuario si desea arriesgar. En caso afirmativo le pide las cartas del arriesgo y devuelve
        una tupla (personaje, arma, lugar),    en caso negativo devuelve None'''
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
        '''Muestra la mano de un jugador'''
        print "Tu mano es:"
        for carta in mano:
            print carta,
        print
    
    def mostrar_listado(self, listado):
        '''Muestra el listado de cartas que aun no vio un determinado jugador'''
        print "Las cartas que aun no viste son:"
        print listado
    
    def mostrar_dados(self, resul):
        '''Le muestra al usuario el resultado de la lanzada de dados'''
        print "Tiraste un....", resul
