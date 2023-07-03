lista = [[],[],[]]
soma_pares = int()
soma_3_coluna = int()
maior_valor_2_linha = int()

print("-="*25)
print("SOMANDO NUMEROS DA MATRIZ".center(50))
print("-="*25)



for x in range(3):
    for y in range(3):
        entrada = int(input(f"Digite um numero para [{x}, {y}]: "))
        lista[x].append(entrada)
        if entrada %2 == 0:
            soma_pares += entrada

for x in range(3):
    soma_3_coluna += lista[x][2]
for x in range(3):
    if maior_valor_2_linha < lista[1][x]:
        maior_valor_2_linha = lista[1][x]

print()

print(f"[{lista[0][0]:^5}] [{lista[0][1]:^5}] [{lista[0][2]:^5}]")
print(f"[{lista[1][0]:^5}] [{lista[1][1]:^5}] [{lista[1][2]:^5}]")
print(f"[{lista[2][0]:^5}] [{lista[2][1]:^5}] [{lista[2][2]:^5}]")

print(f"A soma dos valores pares é: [{soma_pares}]")
print(f"A soma dos valores da terceira coluna é: [{soma_3_coluna}]")
print(f"O maior valor da segunda linha é: [{maior_valor_2_linha}]")

print("-="*25)
print("Fim.".center(50))
print("-="*25)