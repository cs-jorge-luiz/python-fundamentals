#!/usr/bin/python

usuarios = []
senhas = []
opcao = ""

while (opcao != "3"):
    print "\n1 - Cadastrar usuario"
    print "2 - Acessar Sistema"
    print "3 - Sair do Sistema\n"
    opcao = raw_input("Escolha uma opcao (1-3): ")
    
    if (opcao == "1"):
        
        new_user = raw_input("Cadastre o nome do usuario: ")
        new_psw = raw_input("Informe a senha: " )
        usuarios.append(new_user)
        senhas.append(new_psw)
        continue
    
    elif (opcao == "2"):
        
        user = raw_input("Digite o nome do usuario: ")
        password = raw_input("Digite a senha: ")
        
        for u in usuarios:
            if (user == u) and (password == senhas[usuarios.index(u)]):
                print "\nAcesso Liberado!"
                break
            elif (user == u) and (password != senhas[usuarios.index(u)]):
                print "\nSenha Incorreta!"
                break
            else:
                print "Usuario nao encontrado"
                break
    
    elif (opcao == "3"):
        print "Sistema encerrado. Fim do programa."
        break
