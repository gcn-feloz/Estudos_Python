
print("-="*25)
print("LISTAS DE ESTRUTURAS COMPOSTAS".center(50))
print("-="*25)

entrada = 'a'
pessoas = list()
dados = list()
menor_peso = int()
maior_peso = int()

def adiciona_pessoa():
    dados.clear()
    while True:
        entrada = input("Nome: ")
        dados.append(entrada)
        break
    while True:
        try:
            entrada = int(input("Peso: "))
            dados.append(int(entrada))
            break
        except ValueError:
            print("Digite um peso válido.")
    pessoas.append(dados[:])



while entrada not in 'nN':
    adiciona_pessoa()
    entrada = input("Deseja adicionar mais uma pessoa? [S/N]: ")




print(pessoas)



print()
print("-="*25)
print()
print(f"Ao todo você cadastrou {len(pessoas)} pessoas.")

for x in pessoas:
    print(x[1])
    if x[1] > maior_peso:
        maior_peso = x[1]
print(f"O maior peso foi de [{maior_peso}Kg]. Peso de: ", end='')
for x in pessoas:
    if x[1] == maior_peso:
        print(x[0], end=", ")
print("Fim.")



menor_peso = maior_peso
for x in pessoas:
    if x[1] < menor_peso:
        menor_peso = x[1]
print(f"O menor peso foi de [{menor_peso}Kg]. Peso de: ", end="")
for x in pessoas:
    if x[1] == menor_peso:
        print(x[0], end=", ")
print("Fim.")

print("-="*25)
print("-="*25)

