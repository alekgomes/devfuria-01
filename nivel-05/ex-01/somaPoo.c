// Código que retorna o dobro de um numero utilizando POO

#include <iostream>
#include <assert.h>

class Calc {
public:
    int dobro(int num) {
    	return num * 2;
    }
};

void testDobro() {
    Calc c;

    assert(10 == c.dobro(5));
    assert(20 == c.dobro(10));
}

int main() {
    testDobro();
    
}