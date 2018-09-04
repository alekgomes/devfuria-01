# Codigo que encontra fatorial recursividade

def fatorial(n):
	if (n == 0 or n == 1):
		return 1
	else:
		return n * fatorial(n-1)

assert fatorial(2) == 2
assert fatorial(4) == 24
assert fatorial(6) == 720