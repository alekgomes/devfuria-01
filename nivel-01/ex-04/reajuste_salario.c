#include <stdio.h>
#include <assert.h>

float reajustar_salario(float salario, float reajuste) {
    return salario * reajuste;
}

int main (){
    
    assert(150.0f == reajustar_salario(1000, 0.15));

    return 0;
}