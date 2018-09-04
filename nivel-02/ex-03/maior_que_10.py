#-*- coding:utf-8 -*-

def encontra(numero):
	if (numero > 10):
		return True
	elif (numero < 10):
		return False
	else:
		return 10

assert True == encontra(14)
assert False == encontra(9)
assert 10 == encontra(10)