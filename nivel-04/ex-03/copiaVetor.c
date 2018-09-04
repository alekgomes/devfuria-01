// Código para copiar vetor

#include <stdio.h>
#include <assert.h>

void main(){
	int vetor1 [3] = {3, 2, 1};
	int vetor2 [3];

	for(int i = 0; i < 3; i++){
		vetor2[i] = vetor1[i]; 
	}
	assert(vetor1[0] == vetor2[0]);
	assert(vetor1[1] == vetor2[1]);
	assert(vetor1[2] == vetor2[2]);
}