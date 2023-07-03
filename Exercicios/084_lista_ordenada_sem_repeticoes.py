lista = list()

print("-="*25)
print("LISTA ORDENADA SEM REPETIÇÕES".center(50))
print("-="*25)

print(len(lista))

while True:
    print()
    print(f"lista: {lista}")
    print()
    entrada = int(input(f"Digite o {len(lista)+1}º valor: "))
    if entrada == 0:
        break
    elif len(lista) == 0:
        lista.append(entrada)
    elif entrada not in lista:
        if entrada > max(lista):
            lista.append(entrada)
            print(f"Numero {entrada}, adicionado no final da lista.")
        else:
            for pos, val in enumerate(lista):
                if entrada < val:
                    lista.insert(pos,entrada)
                    print(f"Inserindo [{entrada}], na posição [{pos}] da lista.")
                    break
    else:
        print("Número já digitado, escolha outro.")

print("Imprimindo lista:")
print(lista)











print("-="*25)
print("fim!".center(50))
print("-="*25)