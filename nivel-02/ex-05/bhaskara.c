// Código para encontrar as raízes de uma 
// equação de 2° grau

#include <stdio.h>
#include <assert.h>
#include <math.h>

int delta (int a, int b, int c){
	return b*b - (4*a*c);
}

int x1 (int a, int b, int c){
	return (-b + sqrt(delta(a, b, c)))/2*a;
}
	
int x2 (int a, int b, int c){
	return (-b - sqrt(delta(a, b, c)))/2*a;
}

int main(){
	int a, b, c;
	a = 1;
	b = 0;
	c = -16;

	assert(64 == delta(a, b, c));
	assert(4 == x1(a, b, c));
	assert(-4 == x2(a, b, c));
}

