# Encontra valor repetido dentro de um vetor

vetor = [1, 5, 8, 10, 8, 11]
repetidos = 0

i = 0
while i < len(vetor):         # Pegando um elemento do vetor
	for c in vetor[i+1:]:	  # Pegando uma comparação de i para frente
		if vetor[i] == c:     # Verificando igualdade
			repetidos += 1    # Se igual, soma em repetidos
	i += 1                    

if (repetidos > 0):        
	print('Elementos repetidos: {}'.format(repetidos))
else:
	print('Não existem elementos repetidos')

		
#assert repetido == True , 'existe vetor repetido' 

