lista = [[],[]]


for x in range(7):
    entrada = int(input(f"Digite o {x+1}º valor: "))
    if entrada %2 == 0:
        lista[0].append(entrada)
    if entrada %2 == 1:
        lista[1].append(entrada)
    

print("-="*25)
print(f"Os numeros pares digitados foram: {sorted(lista[0])}")
print("-="*25)
print(f"Os numeros impares digitados foram: {sorted(lista[1])}")
print("-="*25)