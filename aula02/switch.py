#!/usr/bin/python

def func1():
    print "Entrou na funcao1"

def func2():
    print "Entrou na funcao2"

def func3():
    print "Entrou na funcao3"

def switch(x):
    dict_func = {1:func1,2:func2,3:func3}
    dict_func[x]()

'''
outra forma de implementar o switch

if x == 1:
    func1()
elif x == 2:
    func2()
elif x == 3:
    func3()
else
    print "Opcao Invalida"
'''

x = input("Digite um valor entre 1 e 3: ")

switch(x)
