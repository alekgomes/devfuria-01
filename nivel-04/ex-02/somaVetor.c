// Código para somar membros de um vetor

#include <stdio.h>
#include <assert.h>

//            vetor    ,tamanho do vetor
int somaVetor(int vetor[], int tam){
	int soma = 0;
	for(int i = 0; i < tam; i++){
		soma = soma + vetor[i];
	}
	return soma;
}

void main(){
	int vetor[4];

	vetor[0] = 1;
	vetor[1] = 2;
	vetor[2] = 3;
	vetor[3] = 4;

	assert(10 == somaVetor(vetor, 4));

}