#-*- coding:utf-8 -*-

def par_ou_impar(numero):
	if (numero %2 ==0):
		par = True
		return par
	else:
		par = False
		return par

assert True == par_ou_impar(10)
assert False == par_ou_impar(11)