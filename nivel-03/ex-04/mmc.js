var assert = require('assert');

var mmc = function(num1, num2) {
    var resto, a, b;

    a = num1;
    b = num2;

    do {
        resto = a % b;

        a = b;
        b = resto;

    } while (resto != 0);

    return (num1 * num2) / a;
}

//
// Testes
//
try {

    assert.equal(60, mmc(12, 20));

} catch(e) {
    console.log(e);
}