// Somar dígitos de um algarismo em C

#include <assert.h>
#include <stdio.h>
#include <math.h>

int soma = 0;

int somar_digitos(int num){
	int resto;
	if (num >= 10){
		resto = num % 10;	
		soma += resto;
		num = floor(num/10);
		somar_digitos(num);
	}
	else{
	soma += num;
	//printf("%d\n", soma);
	return soma;
	}
	
}

void main(){
	assert(10 == somar_digitos(325));
	soma = 0;
	assert(11 == somar_digitos(29));
	soma = 0;
	assert(11 == somar_digitos(2018));
	soma = 0;
	assert(9 == somar_digitos(333));
	soma = 0;
}