#-*-coding:utf-8-*-

def calcula_preco(custo_de_fabrica):
	percentual_imposto = custo_de_fabrica*45/100
	percentual_distribuidor = custo_de_fabrica * 28/100
	preco_final = custo_de_fabrica + percentual_imposto + percentual_distribuidor
	return preco_final

assert 173 == calcula_preco(100)  	