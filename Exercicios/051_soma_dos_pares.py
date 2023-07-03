import random

numeros = int(input("Digite o numero de numeros para gerar: "))
list_numeros = []
list_pares = []
soma_pares = int()
qnt_pares = int()

for x in range(0,numeros):
    list_numeros.append(random.randint(0,10000))
print(f"A lista foi criada com {numeros} nºs aleatorios.")
print(list_numeros)

for x in list_numeros:
    if x % 2 == 0:
        print(f"Numero par encontrado: {x}")
        list_pares.append(x)
        qnt_pares += 1

print(f"No total foram encontrados [{qnt_pares}] numeros pares.")
print("A lista de numeros pares gerada foi:")
print(list_pares)


for x in list_pares:
    soma_pares += x

print(f"Somando todos os valores pares: {soma_pares}")

