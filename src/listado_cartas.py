import os


class ListadoCartas(object):
    """Representa el listado de cartas que un jugador aun no visualizo. Permite llevar cuenta de las cartas
    que ya se vieron, para saber cuales conviene consultar."""
    def __init__(self, personajes_inicial, armas_inicial, lugares_inicial):
        """Recibe un iterable para las cartas de personajes, armas y lugares."""
        self.personajes = personajes_inicial[:]
        self.armas = armas_inicial[:]
        self.lugares = lugares_inicial[:]
    
    def agregar(self, cadena, cartas, nombre):
        cadena += nombre + ":" + os.linesep
        for carta in cartas:
            cadena += carta + os.linesep
        cadena += "------" + os.linesep
        return cadena
    
    def __str__(self):
        """Convierte el listado en una cadena"""
        return self.agregar(self.agregar(self.agregar("", self.personajes, "Personajes"), self.armas, "Armas"), self.lugares, "Lugares")
    
    def sacar_de(self, tipo, carta):
        if carta in tipo:
            tipo.remove(carta)
                
    def sacar_carta(self, carta):
        """Saca una determinada carta de los listados de personajes, armas y lugares (los marca como "vistos")"""
        self.sacar_de(self.personajes, carta)
        self.sacar_de(self.armas, carta)
        self.sacar_de(self.lugares, carta)
