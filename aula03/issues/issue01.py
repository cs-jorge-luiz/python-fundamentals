#!/usr/bin/python

import sys

def cadastrarUsuario():
    global usuarios
    dict_usuario = {"login":"","senha":""}
    dict_usuario["login"] = raw_input("Cadastre o nome do usuario: ")
    dict_usuario["senha"] = raw_input("Informe a senha: " )
    usuarios.append(dict_usuario)

def acessarSistema():
    global usuarios
    for u in usuarios:
        print "lista:"
        print "%s "%u["login"]
        
    print "-= Sistema de Autenticacao =-"
    username = raw_input("Digite o nome do usuario: ")
    passwd = raw_input("Digite a senha: ")    
    for u in usuarios:
        if u["login"] == username and u["senha"] == passwd:
            print "Usuario autenticado com Sucesso"
            break
        else:
            print "Falha ao autenticar!"
            break
    else:
        print "Usuario nao encontrado"


def menu():
    try:
        print " \
            1 - Cadastrar usuario\n \
            2 - Acessar Sistema\n \
            3 - Sair do Sistema\n"

        opcao = input("Escolha uma opcao (1-3): ")
        return opcao
    except Exception as e:
        print "Erro: %s"%e
        return 3

def sairSistema():
    print "Saindo do Sistema ..."
    sys.exit()

def switch(x):
    try:
        dict_options = {1:cadastrarUsuario,2:acessarSistema,3:sairSistema}
        dict_options[x]()
    except Exception as e:
        print "Opcao Invalida"


usuarios = []

if __name__ == '__main__':

    while True:
        switch(menu())
