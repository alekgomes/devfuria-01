# soma dois numeros usando OO

class Calc(object):
	'Uma simples classe'
	def __init__(self, num):
		self.num = num
	def dobro(self):
		return self.num*2

'''Instanciando classes'''
c = Calc(2) 
d = Calc(3)

'''Testando classes'''
assert  c.dobro() == 4
assert  d.dobro() == 6