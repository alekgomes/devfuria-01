#include <stdio.h>
#include <assert.h>

//
// Retorna o custo final da fabricação de um carro
//
float custoFinal(float precoProducao) {
    float custoDistruidor = precoProducao * 28/100;
    float custoImposto = precoProducao * 45/100;
    return precoProducao + custoImposto + custoDistruidor;
}

//
// Teste
//
int main() {

    assert(17300.0f == custoFinal(10000));

    return 0;

}