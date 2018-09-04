#-*- coding:utf-8 -*-

import math

def calcula_delta(a, b, c): 
	delta = (b*b)-(4*a*c)
	return delta

def calcula_x1(a, b, c):
	delta = calcula_delta(a, b, c)
	x1 = (-b + math.sqrt(delta))/2*a
	return x1

def calcula_x2(a, b, c):
	delta = calcula_delta(a, b, c)
	x2 = (-b - math.sqrt(delta)/2*a)
	return x2
	
a = 1
b = 0
c = -16

assert (64 == calcula_delta(a, b, c))
assert (4 == calcula_x1(a, b, c))
assert (-4 == calcula_x2(a, b, c))
