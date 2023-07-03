lista = list()

print("-="*25)
print("EXTRAINDO DADOS DE UMA LISTA".center(50))
print("-="*25)


while True:
    entrada = int(input("Digite um valor: "))
    if entrada == 0:
        break
    if entrada not in lista:
        lista.append(entrada)
    else:
        print("Número já incluso na lista, escolha outro.")

print(f"O numero de itens da lista é: {len(lista)}")
print(f"Os valores da lista em ordem Decrescente: {sorted(lista, reverse=1)}")
if 5 in lista:
    print(f"O valor [5] está na lista.")
else:
    print(f"O valor [5] não está na lista.")









print("-="*25)
print("FIM".center(50))
print("-="*25)




