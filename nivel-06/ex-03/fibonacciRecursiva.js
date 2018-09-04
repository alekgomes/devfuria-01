// Considere a sequência de Fibonacci sendo fibo = [1, 1, 2, 3, 5, 8, ...]
// e n sendo o enésimo termo da sequência.

var assert = require('assert');

function fibo(n) {
    if(n == 0){
        return 1;
    }
    if(n <= 2){
        return n;
    }else{
        return fibo(n - 1) + fibo(n - 2);        
    }
}
    

try {

    assert.equal(1, fibo(0));
    assert.equal(1, fibo(1));
    assert.equal(2, fibo(2));
    assert.equal(3, fibo(3));
    assert.equal(5, fibo(4)); 
    assert.equal(8, fibo(5)); 
    assert.equal(13, fibo(6)); 

} catch(e) {
    console.log(e);
}
