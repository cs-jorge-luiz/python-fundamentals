#!/usr/bin/python

grupos = ["tecnologia","vendas","diretoria","treinamento","administrativo"]

for g in grupos:
    if g == "diretoria":
        print "Diretoria nao precisa alterar a senha"
        continue
    print "Usuarios do grupo [ %s ] precisam alterar a senha"%g
