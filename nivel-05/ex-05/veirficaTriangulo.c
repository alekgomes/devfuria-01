
#include <iostream>
#include <assert.h>

class Triangulo {
public:
    int a, b, c;

    bool validarForma() {
        if((a + b) > c){
            if((a + c) > b){
                if((c + b) > a){
                    return true;
                }
            }
        }
        else{
            return false;
        }
    }
};

//
// Teste unitários...
//
void testValidarFormaCasoPositivo() {
    Triangulo triangulo;
    triangulo.a = 3;
    triangulo.b = 4;
    triangulo.c = 5;
    assert(triangulo.validarForma());
}

void testValidarFormaCasoNegativo() {
    Triangulo triangulo;
    triangulo.a = 1;
    triangulo.b = 4;
    triangulo.c = 5;
    assert(!triangulo.validarForma());
}

//
// Início do programa
//
int main() {
    testValidarFormaCasoPositivo();
    testValidarFormaCasoNegativo();
    return 0;
}