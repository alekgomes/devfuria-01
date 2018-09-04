# Encontra sequencia de Fibonacci resursivamente

# num = posição de um numero na sequência

def fib(i):
	if i == 0:
		return 0
	elif i == 1:
		return 1
	else:
		return fib(i-1) + fib(i-2)

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
