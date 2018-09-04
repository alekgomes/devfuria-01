# Encontrar áreas quadrada e cúbica 

class Objeto(object):                       # Criareamos classes sem atributos
	def area_quadrada(self, lado1,lado2):	# pois passaremos os atributos de forma dinâmica
		return lado1 * lado2 				

	def area_cubica(self, lado1, lado2, lado3):
		return lado1 * lado2 * lado3				
													
'''Instanciando a classe Objeto = Criar objeto'''
teste = Objeto() 								

'''Valores passados dinamicamente, como parâmetros'''
assert teste.area_quadrada(2, 8) == 16    
assert teste.area_cubica(1, 2, 3) == 6	  