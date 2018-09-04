# Encnotrar quantidade de vogais de uma frase # 

vogais = ['a', 'e', 'i', 'o', 'u']

frase = 'essa e uma frase teste'


def encontra_vogais(frase):	
	contador = 0
	for l in frase:		
		for v in vogais:			
			if l == v:
				contador += 1
	return contador
	

assert encontra_vogais(frase) == 9, 'A frase tem 9 vogais'
