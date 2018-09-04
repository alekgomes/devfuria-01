var assert = require('assert');

var vet    = [6, 10, 4, 21, 9],
    iMaior = 0,
    iMenor = 0,
    i = 0;

for(i = 0; i < vet.length; i++) {
    if (vet[i] > vet[iMaior]) {
        iMaior = i;
    }

    if (vet[i] < vet[iMenor]) {
       iMenor = i;
    }
}

//
// Seu teste
//
try {

    assert.equal(3, iMaior);
    assert.equal(2, iMenor);

} catch(e) {
    console.log(e);
}