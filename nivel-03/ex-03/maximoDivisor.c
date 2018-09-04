// Encontra o máximo divisor comum entre dois numeros

#include <stdio.h>
#include <assert.h>

int mdc(int a, int b){
	int resto;

	do{
		resto = a % b;
		a = b;
		b = resto;
	}while (resto != 0);

	return a;
		
}

void main(){
	assert(3 == mdc(24, 9));
    assert(10 == mdc(30, 20));
}