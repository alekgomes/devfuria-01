# exercicio para comparar duas strings usando
# laços de repetição

a = 'abacaxi'
b = 'amarelo'
c = 'abacaxi'
d = 'amarelo2'

def encontra_igual(str1, str2):
	if len(str1) != len(str2):         # Strings com tamanhos diferentes não
		return False                   # são iguais
	else:
		i = 0
		while i < len(str1): 
			if (str1[i] != str2[i]):  
				return False
			i += 1
	return True




assert encontra_igual(a,c) == True
assert encontra_igual(a,b) == False
assert encontra_igual(b,d) == False
