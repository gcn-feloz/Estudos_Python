qnt = int(input("Digite a quantidade de numeros:"))
lista = []
par = int()

for x in range(0,qnt):
    lista.append(x)

print(lista)
print("A lisa foi gerada.")

for x in lista:
    if x % 2 == 0:
        print(f"O número {x}, é par.")
        par += 1

print(f"Nessa lista foram encontrados {par} numeros pares.")