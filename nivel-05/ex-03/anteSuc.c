// Treino utlizando POO

#include <iostream>
#include <assert.h>

class Calc {
public:

    // Retorna o antecessor de um número
    int antecessor(int num) {
        return num - 1;
    }

    // Retorna o sucessor de um número
    int sucessor(int num) {
        return num + 1;
    }
};


void testAntecessor() {
    Calc c;
    assert(9 == c.antecessor(10));
}

void testSucessor() {
    Calc c;
    assert(11 == c.sucessor(10));
}


int main() {
    testAntecessor();
    testSucessor();

}
