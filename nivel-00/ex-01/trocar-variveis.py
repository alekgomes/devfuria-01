# -*- coding: utf-8 -*-

#
# Variáveis
#
a = 999
b = 555

#
# Sua lógica
#
temp=b;
b=a;
a=temp; 



#
# Testes
#
assert a == 555
assert b == 999