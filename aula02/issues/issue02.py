#!/usr/bin/python

usuarios=[]

opcao = ""

while True:
    print " \
           1 - Cadastrar usuario\n \
           2 - Acessar Sistema\n \
           3 - Sair do Sistema\n"

    opcao = input("Escolha uma opcao (1-3): ")
    
    if (opcao == 1):
        dict_usuario= {"login":"","senha":""}
        dict_usuario["login"] = raw_input("Cadastre o nome do usuario: ")
        dict_usuario["senha"] = raw_input("Informe a senha: " )
        usuarios.append(dict_usuario)
    
    elif (opcao == 2):
        
        login = raw_input("Digite o nome do usuario: ")
        senha = raw_input("Digite a senha: ")
        
        for u in usuarios:
            if u["login"] == login and u["senha"] == senha:
                print "Usuario autenticado com Sucesso"
                break
            elif u["login"] == login and u["senha"] != senha:
                print "Senha Incorreta!"
                break
            else:
                print "Usuario nao encontrado"
                break
            
    elif (opcao == 3):
        print "Sistema encerrado. Fim do programa."
        break
