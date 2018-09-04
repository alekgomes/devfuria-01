
#include <iostream>
#include <assert.h>

class Juros {
public:
    float capital, taxa, total;
    int meses;

    int simples(){
        return capital * taxa * meses;
    }
};

//
// Teste Unitário
//
void testJurosSimples() {

    Juros juros;

    juros.capital = 16000;
    juros.taxa    = 0.04;
    juros.meses = 4;

    assert(2560 == juros.simples());
}

//
// Início do programa
//
int main() {
    // Executando o teste unitário
    testJurosSimples();
    return 0;
}