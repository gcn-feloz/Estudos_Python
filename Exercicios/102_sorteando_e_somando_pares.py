import sys
from random import randint, uniform
from time import sleep

numeros = []
soma_n_pares = 0

def cabeçalho(txt,sep):
    print((sep)*(len(txt)+10))
    print((txt.center)(len(txt)+10))
    print((sep)*(len(txt)+10))

def gerar_numeros(n):
    numeros.clear()
    for x in range(n):
        numeros.append(randint(1,99))
        print(numeros[x], end=", ")
        sys.stdout.flush()
        sleep(uniform(0.25,1))
    print("Fim.")

def soma_pares(*n):
    global soma_n_pares
    for x in n:
        for y in x:
            if y %2 == 0:
                soma_n_pares += y

cabeçalho('Sorteando Numeros e Somando Pares','-')

while True:
    gerar_numeros(int(input("Gerar quantos números? ")))
    soma_pares(numeros)
    print(f"A Soma dos números pares é: {soma_n_pares}")
    if input("Continuar [s/n]") in 'nN':
        break