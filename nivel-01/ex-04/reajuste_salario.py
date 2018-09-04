#-*- coding:utf-8 -*-

def calcula_salario(salario, reajuste):
	aumnto = salario * reajuste
	novo_salario = salario + aumnto
	return novo_salario

assert 115 == calcula_salario(100, 0.15)