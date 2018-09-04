#include <stdio.h>
#include <assert.h>

//
// Converte fahrenheit em celsius
//
float toCelsius(float fahrenheit) {
	float celsius = 5*((fahrenheit-32)/9);
	return celsius;
}

//
// Converte celsius em fahrenheit
//
float toFahrenheit(float celsius) {
	float fahrenheit = (celsius * 9/5) + 32;
	return fahrenheit;
}

//
// Testes
//
int main (){

    float celsius    = 100;
    float fahrenheit = 212;

    assert(celsius == toCelsius(fahrenheit));
    assert(fahrenheit == toFahrenheit(celsius));

    return 0;
}