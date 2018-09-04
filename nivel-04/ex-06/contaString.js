var assert = require('assert');

function contaString(str) {
	return str.length;
}
try {

    assert.equal(7, contaString("palavra"));
    assert.equal(8, contaString("palavras"));

} catch(e) {
    console.log(e);
}