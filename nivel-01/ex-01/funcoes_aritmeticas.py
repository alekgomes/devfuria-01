# -*- coding: utf-8 -*-

# as funções são tão pequenas e tão concisas
# que nem precisam de comentários

def somar(num, add):
    soma = num + add
    return soma

def subtrair(num, sub):
    subtrair = num - sub
    return subtrair

def multiplicar(num, mult):
    multiplica = num * mult
    return multiplica

def dividir(num, divisor):
    divide = num/divisor
    return divide

#
# Testes
# 
assert 12 == somar(10, 2)
assert 8 == subtrair(10, 2)
assert 20 == multiplicar(10, 2)
assert 5 == dividir(10, 2)