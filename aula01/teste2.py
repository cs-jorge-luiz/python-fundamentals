#!/usr/bin/python

nome = raw_input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

#print "Voce e o "+nome+" e a sua idade e", idade

print "Voce e o %s e a sua idade %s"%(nome,idade) 

'''
Caso voce queria utiliza o (+) para a idade
voce tera de fazer um casting do valor da variavel
para string

print "Voce e o"+nome+" e a sua idade e"+str(idade)
'''
