var assert = require('assert');

var somarLista = function(lista){
    var soma = 0;
    for(var i = 0; i < lista.length; i++){
        soma += lista[i];
    }
    return soma;
}
//
// Seu teste
//
try {

    lista = [5, 10, 15, 20]
    assert.equal(50, somarLista(lista));

} catch(e) {
    console.log(e);
}