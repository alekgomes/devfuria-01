// Código para concatenar duas strings

#include <stdio.h>
#include <assert.h>
#include <string.h>

void concatenar(char s[], char t[]) {
    int i = 0, j = 0;

    while (s[i] != '\0') {
        i++;
    }

    while ((s[i++] = t[j++]) != '\0');
}

int main() {

    char str1[] = "hello ";
    char str2[] = "world";

    concatenar(str1, str2);

    assert(strcmp("hello world", str1) == 0);

    return (0);
}

