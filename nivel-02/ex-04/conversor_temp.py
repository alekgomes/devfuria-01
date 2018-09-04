#-*- coding:utf-8 -*- 

# Sabendo que 	C = 5/9 * (F-32)
#               F = 9/5 * (C+32)

def c_para_f (celsius):
	f = (celsius*9/5) + 32
	return f

def f_para_c (fahrenheit):
	c = ((fahrenheit-32)/9)*5
	return c

celsius    = 100
fahrenheit = 212 

assert celsius == f_para_c(fahrenheit)
assert fahrenheit == c_para_f(celsius) 


