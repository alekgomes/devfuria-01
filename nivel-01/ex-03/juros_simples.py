#-*- coding:utf-8 -*- 

def calcula_juros(capital, taxa_mensal, meses):
	juros = capital * taxa_mensal * meses   
	total = capital + juros
	return total

assert 116 == calcula_juros(100, 0.04, 4)