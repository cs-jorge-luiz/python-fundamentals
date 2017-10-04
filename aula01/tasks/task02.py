#!/usr/bin/python

'''

Task 02 - Somente um usuario especificado pode logar

Agora que voce ja fez um sistema de login basico, so sera possivel fazer a
autenticacao de usuarios previamente definidos no nosso sistema.

Para isso precisamos ter duas variaveis que vao armazenar um usuario e
uma senha especificadas pelo programador.

Por exemplo: usuario = arthur.dent senha = mochileiro

Se o usuario informado for igual ao usuario especificado no sistema e a senha
desse usuario for igual a senha especificada no sistema. Aparecera a mensagem:

Usuario Autenticado com Sucesso!

Seja Bem Vindo [Usuario]

Caso contrario aparecera:

Acesso Negado

'''

user = "arthur.dent"
password = "mochileiro"

login = raw_input("Digite seu login: ")
senha = raw_input("Digite sua senha: ")

if (login == user) and (senha == password):
    print "Usuario Autenticado com sucesso! \nSeja Bem Vindo %s " %login
else:
    print "Acesso Negado!"
