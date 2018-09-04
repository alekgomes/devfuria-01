# Retornar os índices do maior e menor elemento 
# em uma lista utlizando recursos da linguagem
# como ENUMARATE

lista = [4, 9, 2, 11, 32, 7]
i_maior = 0
i_menor = 0

for index, value in enumerate(lista):
	if lista[index] >= lista[i_maior]:
		i_maior = index
	if lista[index] <= lista[i_menor]:
		i_menor = index

assert i_maior == 4
assert i_menor == 2