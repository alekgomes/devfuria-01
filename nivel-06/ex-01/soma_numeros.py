# Soma numeros com recursão 

def soma(n):
	if (n == 0):               
		return n               # Caso base
	else:
		return n + soma(n-1)   # fórmula geral do problema


assert soma(4) == 10
assert soma(1) == 1 