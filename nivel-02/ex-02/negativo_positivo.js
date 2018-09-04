var assert = require('assert');

var ehPositivo = function(numero) {
    if(numero >= 0) {
        return 1;
    } else {
        return 0;
    }
}

try {
    assert.equal(1, ehPositivo(100));
    assert.equal(1, ehPositivo(0));
    assert.equal(0, ehPositivo(-100));
} catch(e) {
    console.log(e);
}