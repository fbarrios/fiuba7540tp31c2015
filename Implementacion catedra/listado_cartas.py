import os


class ListadoCartas(object):
    def __init__(self, personajes_inicial, armas_inicial, lugares_inicial):
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
        return self.agregar(self.agregar(self.agregar("", self.personajes, "Personajes"), self.armas, "Armas"), self.lugares, "Lugares")
    
    def sacar_de(self, tipo, carta):
        if carta in tipo:
            tipo.remove(carta)
                
    def sacar_carta(self, carta):
        self.sacar_de(self.personajes, carta)
        self.sacar_de(self.armas, carta)
        self.sacar_de(self.lugares, carta)


if __name__ == "__main__":
    personajes = ["Barbara", "Alan"]
    lugares = ["Lab A", "Lab B"]
    armas = ["matafuegos", "proyector"]
    listado = ListadoCartas(personajes, armas, lugares)
    listado.sacar_carta("Barbara")
