# copiar_vetor.py
# Exercício para copiar vetor utilizando laço de repetição

vetor1 = [3, 5, 9, 84]

def copia_vetor(vetor1):
	vetor2 = []
	for n in vetor1:
		vetor2.append(n)
	return vetor2

vetor2 = copia_vetor(vetor1)

assert vetor1[1] == vetor2[1], 'Elementos com mesmo índice deve ser iguas'
assert vetor1[3] == vetor2[3], 'Elementos com mesmo índice deve ser iguas'
