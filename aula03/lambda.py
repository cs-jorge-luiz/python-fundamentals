#!/usr/bin/python

def exemplo(*args):
    for a in args:
        print a

def exemplo2(*args):
    if len(args) == 1:
        print "Calculando o quadrado"
        print args[0] * args[0]
    elif len(args) == 3:
        print "Calculando o retangulo"
        print args[0] * args[1] * args[2]

def exemplokw(**kwargs):
    print type(kwargs)
    print kwargs

quadrado = lambda x:x**2

if __name__ == '__main__':
#    exemplo(1,2,3,4)
#    exemplo2(4)
#    exemplo2(3,4,5)
#    exemplokw(nome="Tenis",valor=43.22,categoria="calcado")
    print quadrado(4)   
