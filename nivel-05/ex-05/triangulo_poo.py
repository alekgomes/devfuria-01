# Dado 3 valores quaisquer que representam lado de um triângulo
# descobrir se formam um triangulo ou não

class Triangulo(object):
	def __init__(self, lado1, lado2, lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3

	def verifica(self):
		if (self.lado1 + self.lado2 > self.lado3):
			if(self.lado2 + self.lado3 > self.lado1):
				if(self.lado1 + self.lado3 > self.lado2):
					return True
		else:
			return False
		 

tri = Triangulo(3, 4, 5)
ntri = Triangulo(1, 1, 2)

assert tri.verifica() == True
assert ntri.verifica() == False


	

	
