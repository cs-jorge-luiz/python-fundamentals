#!/usr/bin/python

import sys

def cadastrar_usuario():
    global nome
    global senha
    nome = raw_input("Digite o login do novo usuario: ")
    senha = raw_input("Digite a senha do novo usuario: ")

def acessar_sistema():
    print "-= Autenticacao do Usuario =-"
    login = raw_input("Digite seu login: ")
    passwd = raw_input("Digite a sua senha: ")
    if nome == login and senha == passwd:
        print "Autenticado com sucesso!\nSeja bem vindo %s"%nome
    else:
        print "Acesso Negado!"

def sair_sistema():
    print "Saindo do Sistema..."
    sys.exit()

def menu():
    try:
        print "\
                1 - Cadastrar usuario\n\
                2 - Acessar Sistema\n\
                3 - Sair do Sistema\n"
        opcao = input("Digite a opcao desejada: ")
        return opcao
    except Exception as e:
        print "Erro: %s"%e
        return opcao

def switch(x):
    try:
        dict_options = {1:cadastrar_usuario,2:acessar_sistema,3:sair_sistema}
        dict_options[x]()
    except Exception as e:
        print "Opcao Invalida"

nome = ""
senha = ""

if __name__ == '__main__': 
    ''' Funcao Principal. essa linha e necessaria para outro arquivo utilizar as funcoes. '__main__' se refere ao proprio arquivo'''
    while True:
        switch(menu())

