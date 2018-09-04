// Soma os digitos de um número

var assert = require('assert');

var somarDigitos = function(num) {
    var soma = 0;

    while (num != 0) {
        soma += num % 10;
        num = parseInt(num / 10); 
    }

    return soma;
}

//
// Testes
//
try {

    assert.equal(8, somarDigitos(2015));
    assert.equal(15, somarDigitos(456));

} catch(e) {
    console.log(e);
}