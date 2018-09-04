# Encontra % de votos
'''Aprendi que não podemos ter métodos com o mesmo que variáveis, pois
isso gera erro ao chamar o método'''
class Votos(object):
	def __init__(self, total):
		self.total   = total
		self.validos = 800.0
		self.brancos = 150
		self.nulos   = 50

	def check_validos(self):
		return self.validos / self.total

	def check_brancos(self):
		return self.brancos / self.total

	def check_nulos (self):
		return self.nulos / self.total

eleitores = Votos(1000)

assert eleitores.check_validos() == 0.8
assert eleitores.check_brancos() == 0.15
assert eleitores.check_nulos()   == 0.05