// Exemplo de bubbleSort em C

#include <assert.h>
#include <stdio.h>
#include <stdbool.h>

int bubbleSort(int vet[], int size){
	int aux;

	for(int j = 0; j < (size - 1);j++){
		for(int i = 0; i < (size - 1); i++){
			if (vet[i] > vet[i+1]){
			// troca elementos
			aux = vet[i];
			vet[i] = vet[i+1];
			vet[i+1] = aux;
			}	
		}	
	}	

}

void main(){
	int vet[] = {8, 9, 3, 5, 1};
	bubbleSort(vet, 5);
	printf("%d\n", vet[0]);
	printf("%d\n", vet[1]);
	printf("%d\n", vet[2]);
	printf("%d\n", vet[3]);
	printf("%d\n", vet[4]);
}