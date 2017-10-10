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


if __name__ == '__main__': # essa linha e necessaria para outro arquivo utilizar as funcoes. '__main__' se refere ao proprio arquivo
#    autenticado = autenticacao() 
#    liberar_acesso(autenticado)
    liberar_acesso(autenticacao())
