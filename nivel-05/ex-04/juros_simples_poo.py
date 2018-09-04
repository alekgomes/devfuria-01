# Calcular juros simples utlizando OO

class Juros(object):
	def __init__(self,emprestimo, meses):
		self.emprestimo = emprestimo
		self.meses = meses
		self.taxa = 0.04

	def calcula(self):
		return self.emprestimo * self.meses * self.taxa

c = Juros(16000, 4) # Emprestimo de 16k em 4 meses

assert c.calcula() == 2560