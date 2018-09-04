#-*- coding:utf:8 -*-

def encontra_primo(num):
	encontrou_divisor = False  # variável de referência
	if (num == 2):
		return True
	else:	
		for divisor in range(2, num):
			if (num%divisor == 0):
				encontrou_divisor = True
		if (encontrou_divisor):
			return False      # Se encontrou divisor, não é primo. Return false
		else:
			return True       # Se não encontrou divisor, é primo. Return true
			

## Testes ##
assert True == encontra_primo(11)
assert True == encontra_primo(2)
assert False == encontra_primo (10)
assert False == encontra_primo(15)
