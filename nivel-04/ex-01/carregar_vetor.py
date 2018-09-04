# Código para carregar vetor com inteiros 
# de 1~5 (inclusive)

vetor =[]
def carregar_vetor(vetor):
	for n in range(1,6):
		vetor.append(n)
	return vetor
		
carregar_vetor(vetor)


assert vetor[0] == 1
assert vetor[3] == 4
assert vetor[4] == 5
assert len(vetor) == 5 , 'vetor lenght must be 5'