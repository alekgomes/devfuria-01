var assert = require('assert');


//
// Converte fahrenheit em celsius
//
function toCelsius(fahrenheit){
	c = ((fahrenheit-32)/9)*5
	return c

}

//
// Converte celsius em fahrenheit
//
function toFahrenheit(celsius) {
	f = (celsius*9/5) + 32
	return f

}

//
// Testes
//
try {
    var celsius    = 100
    var fahrenheit = 212

    assert.equal(celsius, toCelsius(fahrenheit), "msg");
    assert.equal(fahrenheit, toFahrenheit(celsius), "msg");
} catch(e) {
    console.log(e);
}