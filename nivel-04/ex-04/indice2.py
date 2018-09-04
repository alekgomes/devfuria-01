# Retornar os índices do maior e menor elemento 
# em uma lista utlizando recursos da linguagem

lista = [4, 9, 2, 11, 32, 7]
i_maior = 0
i_menor = 0

lista.sort()  # É como usar cheat já que altera a lista e o menor
			  # índice sempre será [0] e o maior [-1]

i_maior = lista[-1]
i_menor = lista[0]

assert lista[0] == 2
assert lista[-1] == 32
