from time import sleep
from random import randint
import sys

numeros = []

def cabeçalho(txt,carac):
    print(carac*(len(txt)+10))
    print((txt).center(len(txt)+10))
    print(carac*(len(txt)+10))

def analise(*dados):
    print(f"Foram informados {len(dados[0])} números ao todo;")
    print(f"O maior número informado foi: {max(dados[0][:])}")

def gera_numeros(qnt):
    for x in range(qnt):
        numeros.append(randint(1,99))
        print(numeros[x], end=", ")
        sys.stdout.flush()
        sleep(.2)
    print("Fim.")



cabeçalho("PROCESSANDO LISTA COM FUNÇÃO",'+')
while True:
    gera_numeros(int(input("Gerar quantos números na lista? ")))
    cabeçalho(str(numeros), '-')
    analise(numeros)
    if input("Continuar? [s/n] ") in 'Nn':
        break

