// Retorna o dobro de um número utlizando POO

var assert = require('assert');

function Calc(){

    this.dobro = function(num){
        return num * 2;
    }

};

try {

    var calc = new Calc();
    assert.equal(10, calc.dobro(5));
    assert.equal(50, calc.dobro(25));

} catch(e) {
    console.log(e);
}