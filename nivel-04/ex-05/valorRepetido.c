// Encontra valores repetidos em C

#include <stdio.h>
#include <assert.h>
#include <stdbool.h>

int encontraRepetido(int vet[], int tam){
	bool retorno;
	for(int i = 0; i < tam; i++){
		for(int j = i+1; j < tam; j++){
			if (vet[i] == vet[j]){
				return true;
				break;
			}else{
				retorno = false;
			}			
		}
	}
	return retorno;
}
void main(){

	int vetor[5] = {4, 2, 6, 2, 8};
	int vetor2[6] = {1, 2, 3, 4, 5, 6};

	assert(encontraRepetido(vetor, 5) == true);
	assert(encontraRepetido(vetor2,6) == false);

}