#!/usr/bin/python

def autenticacao(): # parametros - valores esperados 
    print "-= Autenticacao do Usuario =-"
    nome = raw_input("Digite seu login: ")
    senha = raw_input("Digite a sua senha: ")
    if nome == 'jorge' and senha =='123':
        autenticado = True
    else:
        autenticado = False
    return autenticado

def liberar_acesso(auth):
    '''Poderia por exemplo passar um paramentro obrigatorio. Ex: def liberar_acesso(auth=False)'''

    if auth: #poderia ser escrito auth is True, mas como e valor booleano nao ha necessidade
        print "Acesso Permitido"
    else:
        print "Acesso Negado"

def cadastrar_usuario():
    print "Cadastrar usuario"

def acessar_sistema():
    print "Acessar Sistema"

def sair_sistema():
    print "Saindo do Sistema..."

def menu():
    print "\
            1 - Cadastrar usuario\n \
            2 - Acessar Sistema\n \
            3 - Sair do Sistema\n "
    opcao = input("Digite a opcao desejada: ")
    return opcao

def switch(x):
    dict_options = {1:cadastrar_usuario,2:acessar_sistema,3:sair_sistema}
    dict_options[x]()

if __name__ == '__main__': 
    ''' Funcao Principal. essa linha e necessaria para outro arquivo utilizar as funcoes. '__main__' se refere ao proprio arquivo'''
    switch(menu())

