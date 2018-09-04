#-*- coding:utf-8 -*-

def encontra_digito(num):
	a = num
	contador = -1
	while (a >= 1): 
		b = a           # b = 123      | b = 12       | b = 1 
		a = a/10 	    # a = 12       | a = 1        | a = 0
		contador += 1   # contador = 0 | contador = 1 | contador = 2
	retorno = [contador, b] 	
	return retorno

def altera_num(num):
	soma = 0
	while (num > 0):
		retorno = encontra_digito(num)              # [2, 1]
		soma += retorno[1]                          # soma = 1
		num = num - ((10 ** retorno[0])*retorno[1]) # num = 23
	print soma

num = 4
altera_num(num)








