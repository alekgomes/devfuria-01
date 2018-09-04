// Encontrar o índice do maior e do menor digito num vetor

#include <stdio.h>
#include <assert.h>

void main(){
	int vetor[5] = {3, 2, 8, 1, 4};
	int i, iMaior, iMenor;

	iMaior = 0;
	iMenor = 0;

	for(i = 0; i < 5; i++){
		if (vetor[i] > vetor[iMaior]){
			iMaior = i;
		}
		if (vetor[i] < vetor[iMenor]){
			iMenor = i;
		}
	}

	assert(iMaior == 2);
	assert(iMenor == 3);	
}





