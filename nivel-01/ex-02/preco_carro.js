var assert = require('assert');

//
// Retorna o custo final da fabricação de um carro
//
var custoFinal = function(precoProducao) {
	var custoDistribuidor = precoProducao * 28/100
	var custoImposto = precoProducao * 45/100
	return precoProducao + custoImposto + custoDistribuidor
}

//
// Seu teste
//
try {
    assert.equal(17300, custoFinal(10000));
} catch(e) {
    console.log(e);
}