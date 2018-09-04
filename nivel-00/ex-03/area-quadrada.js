var assert = require('assert');

//
// Função que retorna o valor da área
//
var area = function (lado1, lado2) {
    return lado1*lado2;
}

//
// Seu teste
//
try {
    assert.equal(area(3, 9), 27, "deve retornar o área");
} catch(e) {
    console.log(e);
}