#include <stdio.h>
#include <assert.h>
#include <stdbool.h>

bool ehMaiorQue10(int valorQualquer) {
    if (valorQualquer > 10) {
        return true;
    } else {
        return false;
    }
}

int main (){

    assert(true == ehMaiorQue10(17));
    assert(false == ehMaiorQue10(9));

    return 0;
}