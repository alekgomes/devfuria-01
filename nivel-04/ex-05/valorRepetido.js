var assert = require('assert');

var verificaCopia = function(vet) {
    var i;
    for(i = 0; i < vet.length; i++) {
        if(vet.indexOf(vet[i]) != i) {
            return true;
        };
    }
    return false;
}

//
// Seu teste
//
try {

    assert.equal(true, verificaCopia([100, 200, 300, 300, 500]));
    assert.equal(false, verificaCopia([100, 200, 300, 400, 500]));

} catch(e) {
    console.log(e);
}