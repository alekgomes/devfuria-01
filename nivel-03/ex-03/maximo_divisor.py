#-*- coding:utf-8 -*-
##### Encontrar o maior divisor comum entre dois números ##

# 1 - Função que encontra os divisores de dois números
#		-Adicionar divisores na lista 'divisoresA' e 'divisoresB'
# 2 - Ver quais números as lista divicsoresA e divisoresB têm em comum
#	  e selecionar o maior deles como o maior divisor comum entre os dois números

def encontra_divisores(numA, numB):
	divisoresA = []
	divisoresB = []
	
	for a in range(2, numA):                  #Encontra divisores de numA
		if (numA % a == 0):
			divisoresA.append(a)
	for b in range(2, numB):                  #Encontra divisores de numB
		if (numB % b == 0):
			divisoresB.append(b)
	retorno = divisoresA + divisoresB
	return retorno

numA, numB = 10, 15

def encontra_comuns():
	comuns = []
	divisores = encontra_divisores(numA, numB)    # Todos os divisores dos 2 números
	for c in divisores:                           # Seleciona somente os divisores COMUNS 
		if (divisores.count(c) == 2):             # ou seja, aqueles que aparecem duas vezes na lista
			comuns.append(c)

	return max(comuns)                             # Imprime o maior divisor comum

#assert 5 == encontra_comuns()
#assert [2, 5, 3, 5] == encontra_divisores(10, 15)
