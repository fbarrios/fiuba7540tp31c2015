HORARIO = 0
ANTIHORARIO = 1

class Tablero(object):
	def __init__(self, casilleros):
		self.casilleros = casilleros
	
	def __iter__(self):
		for casillero in casilleros:
			yield casillero
	
	def siguiente_sentido_horario(self, pos, movimiento):
		return (pos + movimiento) % len(self.casilleros)
	
	def siguiente_sentido_antihorario(self, pos, movimiento):
		return (pos - movimiento) % len(self.casilleros)
	
	def siguiente(self, pos, movimiento, sentido):
		if sentido == HORARIO:
			return self.siguiente_sentido_horario(pos, movimiento)
		else:
			return self.siguiente_sentido_antihorario(pos, movimiento)
	
	def __getitem__(self, pos):
		return self.casilleros[pos]
	
	def __len__(self):
		return len(self.casilleros)
