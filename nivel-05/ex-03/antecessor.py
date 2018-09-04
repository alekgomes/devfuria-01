# Encontrar antecessor e sucessor de um número
# Fazer utilizando conceitos de POO

class Calc(object):

	def sucessor(self, num):
		return num + 1

	def antecessor(self, num):
		return num - 1

c = Calc()

assert c.sucessor(10) == 11
assert c.antecessor(9) == 8