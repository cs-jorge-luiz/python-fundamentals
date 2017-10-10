#!/usr/bin/python

def autenticacao():# parametros - valores esperados 
    print "-= Autenticacao do Usuario =-"
    nome = raw_input("Digite seu login: ")
    senha = raw_input("Digite a sua senha: ")
    print "Seja bem vindo %s"%nome


if __name__ == '__main__': # essa linha e necessaria para outro arquivo utilizar as funcoes. '__main__' se refere ao proprio arquivo
    autenticacao() # argumentos - valores passados como parametro. Ex: autenticacao(nome,senha)
