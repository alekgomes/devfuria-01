var assert = require('assert');

var vetor = [4, 1, 6, 9, 2]

try {

    assert.equal(4, vetor[0]);
    assert.equal(1, vetor[1]);
    assert.equal(6, vetor[2]);
    assert.equal(9, vetor[3]);
    assert.equal(2, vetor[4]);

} catch(e) {
    console.log(e);
}