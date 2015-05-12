
# Importa el paquete para realizar pruebas automatizadas de Python.
import unittest
from unittest import TestCase

# Importa las clases que se van a probar
from dados import DadoEstandar
from tablero import Tablero


# Definimos una clase que hereda de TestCase por cada Clase que queremos probar.
# Esta clase esta dedicada a probar la clase de DadoEstandar.
class TestDadoEstandar(TestCase):

    # Cada metodo debe probar una funcionalidad de la clase.
    # Este, por ejemplo, verifica que las probabilidades de cada cara son iguales.
    def test_probabilidades_son_equiprobables(self):
        # Dentro de un metodo realizo la prueba:

        # Creo un dado estandar de seis caras.
        dado = DadoEstandar(6)

        # Obtengo sus probabilidades.
        # Este metodo no se usa en el juego pero se agrego para poder correr la prueba.
        probabilidades = dado.obtener_probabilidades()

        prob = probabilidades[0]
        for i in range(1, len(probabilidades)):
            # Se usan los metodos de unittest para hacer verificaciones.
            self.assertEqual(prob, probabilidades[i])

    # Este otro metodo, por ejemplo, verifica que las probabilidades de ocurrencia de
    # cada cara no se puedan modificar.
    def test_probabilidades_no_se_deben_modificar(self):
        dado = DadoEstandar(6)
        probabilidades = dado.obtener_probabilidades()

        # Modifico el resultado devuelto.
        probabilidad_anterior = probabilidades[0]
        probabilidades[0] = probabilidad_anterior + 1

        # Verifico que no se haya modificado su probabilidad dentro del dado.
        self.assertEqual(probabilidad_anterior, dado.obtener_probabilidades()[0])


class TestTablero(TestCase):

    # Prueba que la creacion usando listas de diferentes largos levante una excepcion.
    def test_inicializacion_con_distintos_largos_invalida(self):
        casilleros = ['1', None, '3']
        posiciones = ['1', '2']

        # Estructura que verifica que se levante una excepcion de tipo ValueError
        # dentro del bloque with.
        with self.assertRaises(ValueError):
            Tablero(casilleros, posiciones)

    # Prueba que los casilleros no se puedan modificar desde afuera.
    def test_casilleros_no_se_deben_modificar(self):
        raise NotImplementedError()


# Si este archivo crece mucho quizas sea necesario dividirlo...


# Ejecuta todas las pruebas cuando se ejecute este archivo.
if __name__ == "__main__":
    unittest.main()
