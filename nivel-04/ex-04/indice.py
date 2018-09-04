# Retornar os índices do maior e menor elemento 
# em uma lista usando laço de repetição

lista = [4, 9, 2, 11, 32, 7]
i_maior = 0
i_menor = 0

i = 0 
while i < len(lista):
	if lista[i] >= lista[i_maior]:
		i_maior = i

	if lista[i] <= lista[i_menor]:
		i_menor = i

	i += 1

assert i_maior == 4 , 'Maior elemento é o de índice = 4'
assert i_menor == 2 , 'Menor elemento possui índice = 2'