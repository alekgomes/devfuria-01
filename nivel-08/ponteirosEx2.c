// Utilizando ponteiros

#include <stdio.h>
#include <assert.h>

void main() {

    int x, *y;

    x = 10;    // x armazena 10
    y = &x;    // y recebe REFERÊNCIA para X
    x = 20;    // x é alterado, logo y tbm é, pois y aponta para onde
               // que que seja que X aponte
    
    assert(x == 20);
    assert(*y == 20);
}