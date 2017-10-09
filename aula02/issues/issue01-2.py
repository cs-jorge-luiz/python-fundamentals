#!/usr/bin/python

usuarios = []
senhas = []
opcao = ""

while True:
    print " \
           1 - Cadastrar usuario\n \
           2 - Acessar Sistema\n \
           3 - Sair do Sistema\n"

    opcao = input("Escolha uma opcao (1-3): ")
    
    if (opcao == 1):
        
        new_user = raw_input("Cadastre o nome do usuario: ")
        new_psw = raw_input("Informe a senha: " )
        usuarios.append(new_user)
        senhas.append(new_psw)
        continue
    
    elif (opcao == 2):
        
        user = raw_input("Digite o nome do usuario: ")
        password = raw_input("Digite a senha: ")
        
        for i,u in enumerate(usuarios):
            if u == user:
                if password == senhas[i]:
                    print "Usuario autenticado com Sucesso"
                    break
                else:
                    print "Senha Incorreta!"
                    break
        else:
            print "Usuario nao encontrado"
        
    
    elif (opcao == 3):
        print "Sistema encerrado. Fim do programa."
        break
