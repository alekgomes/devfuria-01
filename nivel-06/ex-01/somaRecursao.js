
var assert = require('assert');

function add(n){
    if (n == 0){
        return n;
    }
    else{
        return n + add(n - 1);
    } 

    // caso recursivo;
}
//
// Testes
//
try {
    assert.equal(15, add(5));
    assert.equal(21, add(6));
    assert.equal(6 , add(3));
} catch(e) {
    console.log(e);
}