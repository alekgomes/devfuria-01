// Código para comparar 2 strings

#include <stdio.h>
#include <assert.h>
#include <stdbool.h>

bool comparaString(char vetor1[], char vetor2[], int size){
	
	for(int i = 0; i < size; i++){
		if(vetor1[i] != vetor2[i]){
			return false;
			break;			
		}
	}
	return true;
}

void main(){
	char string1[] = "palavra qualquer";
	char string2[] = "palavra qualquer";
	char string3[] = "outras qualquers";

	assert(false == comparaString(string1, string3, 16));
	assert(true == comparaString(string1, string2, 16));
	assert(false == comparaString(string2, string3, 16));
}
