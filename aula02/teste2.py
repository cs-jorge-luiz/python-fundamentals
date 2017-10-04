#!/usr/bin/python

idade = 17
carteirinha = True
pais = False

if idade >= 18 and carteirinha is True:
    print "Acesso Liberado!"
elif idade <=17 and pais is True:
    print "Acesso liberado com supervisao dos pais"
else:
    print "Acesso Negado!"
