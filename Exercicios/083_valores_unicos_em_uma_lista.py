lista = list()

print("-="*25)
print("VALORES UNICOS EM UMA LISTA".center(50))
print("-="*25)

while True:
    entrada = input("Digite um numero, ou [0] para sair: ")
    if entrada not in lista and entrada != '0':
        lista.append(entrada)
    else:
        print(f"O numero {entrada}, ja foi informado e não será incluso na lista.")
    if entrada == '0':
        break


print("Imprimindo a lista:")
print(sorted(lista))


print("-="*25)
print("-="*25)