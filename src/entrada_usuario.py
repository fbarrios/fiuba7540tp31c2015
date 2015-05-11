
VER_POSIBILIDADES = "*"


def solicitar_numero(minimo, maximo, mensaje):
    """Obtiene un numero del usuario, entre los valores minimos y maximos."""
    while True:
        valor = raw_input(mensaje)
        if not valor.isdigit():
            print "Error, debe ingresar un valor numerico."
            continue
        valor = int(valor)
        if minimo <= valor <= maximo:
            return valor
        else:
            print "Error, debe ingresar un valor entre", minimo, "y", maximo, "."


def mostrar_posibilidades(posibilidades):
    """Le muestra al usuario las opciones que tiene para realizar su seleccion en un ingreso."""
    for pos, carta in enumerate(posibilidades):
        print str(pos + 1) + ". " + carta


def solicitar_entre_opciones(posibilidades, tipo):
    """Dada una lista de opciones, imprime un mensaje para que el usuario permita seleccionar entre una de ellas.
    Devuelve el indice de la seleccion realizada."""
    while True:
        valor = raw_input("Ingrese " + tipo + ". Si quiere ver todas las posibilidades, ingrese " + VER_POSIBILIDADES + ".\n")
        if not valor.isdigit() and valor != VER_POSIBILIDADES:
            print "Error, debe ingresar un valor numerico."
            continue

        if valor == VER_POSIBILIDADES:
            mostrar_posibilidades(posibilidades)
            continue
        if 1 <= int(valor) <= len(posibilidades):
            return int(valor) - 1
        else:
            print "Error en el ingreso."


def pregunta_si_no(pregunta):
    """Solicita al usuario una entrada por si o por no."""
    pregunta += " S/N\n"
    while True:
        si_no = raw_input(pregunta)
        if si_no.upper() == "S":
            return True
        elif si_no.upper() == "N":
            return False
        print "Error en el ingreso."


def solicitar_nombre_jugador(jugadores, num_jugador):
    """Le solicita al usuario el nombre de un nuevo jugador, verificando que no esta entre los ya ingresados."""
    while True:
        nombre = raw_input("Ingrese nombre del jugador " + str(num_jugador + 1) + ":\n")
        if nombre in jugadores:
            print "Error, ya fue ingresado ese nombre."
            continue

        jugadores.append(nombre)
        return nombre