from random import randint

qnt_numeros = int()
tupla1 = ()

def valida(dados):
    try:
        int(dados)
        return True
    except ValueError:
        return False

def seleciona_qnt():
    global qnt_numeros
    while True:
        entrada = input("Digite a qnt de posições da tupla, ou [0] para sair: ")
        if valida(entrada):
            qnt_numeros = int(entrada)
            break

def cria_tupla():
    global tupla1
    del tupla1
    tupla1 = tuple((randint(0,9) for _ in range(qnt_numeros)))

print()
print("-="*25)
print("ANALISE DE DADOS DE UMA TUPLA".center(50))
print("-="*25)
print()
while True:
    seleciona_qnt()
    if qnt_numeros == 0:
        break
    cria_tupla()
    print(("-"*25).center(50))
    print(f"A 'tupla1' com {qnt_numeros} posições, foi criada, com nºs de 0 à 9:")
    print(tupla1)
    print(("-"*25).center(50))
    print(f"O valor 9 apareceu {tupla1.count(9)} vezes.")
    
    try:
        tupla1.index(3)
        print(f"O valor 3 apareceu na {tupla1.index(3)+1}ª posição")
    except ValueError:
        print(f"O valor 3 não foi encontrado em nenhuma posição.")
    print(("-"*25).center(50))
    print(f"Os valores pares digitados foram: ")
    for x in tupla1:
        if x % 2 == 0:
            print(x, end=", ")
    print("Fim.")
    print(("-"*25).center(50))