// Código para contar uma string

#include <stdio.h>
#include <assert.h>

int contaString(char texto[]){
	int i;
	int contador = 0;

	for(i = 0; texto[i] != '\0'; i++){
		contador++;
	}
	return contador;
}
void main(){

	char texto[] = "palavra";
	char hello[] = "world";

	assert(7 == contaString(texto));
	assert(5 == contaString(hello));
}