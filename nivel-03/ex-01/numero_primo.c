// Código para encontrar número primo em C

#include <stdio.h>
#include <assert.h>
#include <stdbool.h>

int verifica_primo(int num){
	int i, divisores;
	divisores = 0;

	for (i = 1; i <= num; i++){
		if (num % i == 0){
			divisores++;
		}
	}
	if (divisores == 2){
		return true;
	}
	else{
		return false;
	}
}

int main(){
	int a, b, c, d, e;
	a = 3;	b = 2;	c = 4;	d = 28;	e = 17;

	assert(true == verifica_primo(a));
	assert(true == verifica_primo(b));
	assert(false == verifica_primo(c));
	assert(false == verifica_primo(d));
	assert(true == verifica_primo(e));
}