// Código para inverter uma string

#include<stdio.h>
#include<string.h>
#include<assert.h>

int main() {

    char str[] = "abacaxi";
    char temp;
    int i, j;

    i = 0;
    j = strlen(str) - 1;

    while (i < j) {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
        i++;
        j--;
    }

    assert(strcmp("ixacaba", str) == 0);

}