// exemplo SEM uso de ponteiros
#include <stdio.h>
#include <assert.h>

void main() {

    int x, y;

    x = 10;   // valor de x => 10
    y = x;    // valor armazenado em y
    x = 20;   // valor de x alterado

    assert(x == 20);
    assert(y == 10);
}