var assert = require('assert');

var ehMaiorQue10 = function(valorQualquer) {
    if (valorQualquer > 10) {
        return 1;
    } else {
        return 0;
    }
}

try {
    assert.equal(1, ehMaiorQue10(17));
    assert.equal(0, ehMaiorQue10(9));
} catch(e) {
    console.log(e);
}