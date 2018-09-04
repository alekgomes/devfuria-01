// Minimo multiplo comum

#include <stdio.h>
#include <assert.h>

int mmc(int a, int b){
	int resto, mmc;
	int numA = a;
	int numB = b;

	do{
		resto = a % b;
		a = b;
		b = resto;
	}while (resto != 0);

	mmc = (numA*numB)/a;

	return mmc;
}

void main(){
    assert(60 == mmc(12, 20));
    assert(12 == mmc(6,4));
}