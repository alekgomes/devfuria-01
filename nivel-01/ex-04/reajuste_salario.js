var assert = require('assert');

var reajustar_salario = function(salario, reajuste) {
    return salario * reajuste;
}

try {
    assert.equal(150, reajustar_salario(1000, 0.15));
} catch(e) {
    console.log(e);
}