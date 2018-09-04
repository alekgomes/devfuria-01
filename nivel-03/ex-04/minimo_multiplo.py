#-*- coding:utf-8 -*-

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

numA, numB = 10, 20

def encontra_comuns():
	comuns = []
	divisores = encontra_divisores(numA, numB)    # Todos os divisores dos 2 números
	for c in divisores:                           # Seleciona somente os divisores COMUNS 
		if (divisores.count(c) == 2):             # ou seja, aqueles que aparecem duas vezes na lista
			comuns.append(c)

	return min(comuns) 

#assert 2 == encontra_comuns()