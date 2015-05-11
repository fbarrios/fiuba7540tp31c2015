
class Jugador(object):
    """Representa a un jugador manejado por un usuario. Todo el manejo para pedirle y mostrarle cosas al usuario
    se hace utilizando su atributo "pedidos" que se encarga de dichas tareas. En este modulo no puede haber ninguna
    funcion raw_input ni print, ni ninguna semejante."""
    def __init__(self, nombre, posicion_inicial, listado_inicial, dados, pedidos):
        """Recibe su nombre, una posicion inicial, un listado ya inicializado, los dados a usar
        y alguien que le permita hacerle pedidos al usuario, de la manera que correzponda."""
        self.posicion = posicion_inicial
        self.listado = listado_inicial
        self.mano = []
        self.dados = dados
        self.pedidos = pedidos
        self.nombre = nombre
    
    def get_nombre(self):
        """Devuelve el nombre del jugador"""
        return self.nombre
        
    def __eq___(self, otro):
        """Verifica si un jugador es igual a otro jugador. Dos jugadores son iguales
        cuando tienen el mismo nombre"""
        return self.nombre == otro.nombre
    
    def asignar_carta(self, carta):
        """Se le asigna una carta a la mano del jugador. Este la marca como vista en su listado
        de cartas."""
        self.mano.append(carta)
        self.listado.sacar_carta(carta)
    
    def get_posicion(self):
        """Obtiene la posicion del jugador."""
        return self.posicion
    
    def alguna_carta(self, jugada):
        """Se fija si el jugador tiene alguna de las cartas indicadas en la jugada.
        Parametros:
            - jugada: iterable con cartas.
        Salida: si tiene al menos una de las cartas, debe preguntarle al usuario cual
        prefiere mostrarle. Si no tiene ninguna, devuelve None."""
        eleccion = []
        for carta in jugada:
            if carta in self.mano:
                eleccion.append(carta)
        if len(eleccion) == 0:
            return None
        else:
            return self.pedidos.pedir_carta_a_mostrar(self, eleccion)
    
    def jugarsela(self):
        """Devuelve arriesgo del usuario (personaje, arma, jugador), o None si no desea arriesgarse."""
        se_la_juega = self.pedidos.preguntar_arriesgo()
        return se_la_juega
    
    def mover(self, tablero):
        """Lanza los dados y se mueve en algun sentido por el tablero. Le muestra al usuario el resultado de
        haber lanzado los dados, y le pide el sentido en el que debe moverse."""
        lanzamientos = [dado.lanzar() for dado in self.dados]
        self.pedidos.mostrar_dados(lanzamientos)
        horario = self.pedidos.pedir_sentido()
        self.posicion = tablero.siguiente(self.posicion, sum(lanzamientos), horario)
    
    def sugerir(self, tablero, otros_jugadores):
        """Si esta en algun lugar para hacer sugerencias, le pregunta al usuario si desea hacer una.
        En caso afirmativo, le muestra la mano al jugador, le muestra el listado de cartas que aun no vio, 
        le pide la jugada, y le consulta al resto de los jugadores si tiene alguna
        de las cartas.
        Parametros:
            - tablero: tablero del juego.
            - otros_jugadores: un iterable con los demas jugadores, en el orden en el que se les debe consultar."""
        lugar = tablero[self.posicion]
        if lugar is None or not self.pedidos.quiere_consultar(lugar):
            return
        self.pedidos.mostrar_mano(self.mano)
        self.pedidos.mostrar_listado(self.listado)
        
        personaje = self.pedidos.pedir_personaje()
        arma = self.pedidos.pedir_arma()
        
        for jugador in otros_jugadores:
            carta = jugador.alguna_carta( (personaje, arma, lugar) )
            if carta is not None:
                self.pedidos.mostrar_carta(jugador, carta)
                self.listado.sacar_carta(carta)
                return
        self.pedidos.mostrar_no_hay_cartas()
