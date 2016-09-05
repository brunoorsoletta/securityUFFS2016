#!/usr/bin/python
#coding:utf8

# Algoritmo de Diffle-Hellman: 

base = 13
mod  = 17


def start():
	cs = input("Digite a chave secreta: ")
	cs = int(cs)

	print "Codificado: ",((base**cs) % mod)	

	ci = input("Digite a chave intermediaria: ")
	ci = int(ci)

	print "Codificado: ",((ci**cs) % mod)

start()
