#!/usr/bin/python3
def funçao(letra):
    return letra.upper()
letras = ['a', 'Z', 'b', 'c','A']
ordenadas = sorted(letras, key=funçao)

for l in ordenadas:
    print(l)