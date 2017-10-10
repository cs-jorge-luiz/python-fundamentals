#!/usr/bin/python

import sys
import os
import json

def cadastrar_usuario():
    usuarios = []
    if not os.stat('banco.json').st_size == 0:
        with open('banco.json',"r") as f:
            dicionario_usuarios = json.load(f)
        usuarios = dicionario_usuarios["usuarios"]
        dicionario_usuarios["usuarios"] = usuarios
    else:
        dicionarios_usuarios = {"usuarios":usuarios}

    dict_usuario = {"login":"","senha":""}
    dict_usuario["login"] = raw_input("Cadastre o nome do usuario: ")
    dict_usuario["senha"] = raw_input("Informe a senha: " )
    usuarios.append(dict_usuario)

    try:
        with open("banco.json","w") as f:
            json.dump(dicionario_usuarios,f)
    except Exception as e:
        print "Falhou a escrever no arquivo %s"%e

def acessar_sistema():
    if not os.stat('banco.json').st_size == 0:
        with open('banco.json',"r") as f:
            dicionario_usuarios = json.load(f)

    print "\n-= Sistema de Autenticacao =-"
    username = raw_input("Digite o nome do usuario: ")
    passwd = raw_input("Digite a senha: ")

    for u in dicionario_usuarios["usuarios"]:
        if u["login"] == username and u["senha"] == passwd:
            print "Usuario autenticado com Sucesso"
            break
    else:
        print "Usuario nao encontrado"

def sair_sistema():
    print "Saindo do Sistema ..."
    sys.exit()

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


def switch(x):
    try:
        dict_options = {1:cadastrar_usuario,2:acessar_sistema,3:sair_sistema}
        dict_options[x]()
    except Exception as e:
        print "Opcao Invalida"


if __name__ == '__main__':
    while True:
        switch(menu())
