#include <stdio.h>
#include <assert.h>

int fib(int n) {
    if (n == 0)
        return 1;
    if (n <= 2){
    	return n;
    }
    else
        return fib(n - 1) + fib(n - 2);
}

int main() {
    assert(1  == fib(0));
    assert(1  == fib(1));
    assert(2  == fib(2));
    assert(3  == fib(3));
    assert(5  == fib(4));
    assert(8  == fib(5));
    assert(13 == fib(6));
    return 0;
}