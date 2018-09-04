// Código para contas vogais em uma string

#include <stdio.h>
#include <assert.h>

int contaVogal(char vetor[], int size){
	char vogais[] = "aeiou";
	int i, j, contador;
	contador = 0;
	
	for(i = 0; i < size; i++){
		for(j = 0; j < 5; j++){
			if(vetor[i] == vogais[j]){
				contador++;
			}
		}	
	}
	return contador;
}

void main(){
	char vetor1[] = "paluvre";
	char vetor2[] = "lucas alek";

	assert(3 == contaVogal(vetor1, 7));

	assert(4 == contaVogal(vetor2, 10));
}