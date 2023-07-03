print("-="*25)
print("MAIOR E MNOR VALOR DA LISTA".center(50))
print("-="*25)

lista = list()
entrada = str()
maior = menor = int()
c = int()

while entrada != 0:
    c += 1
    entrada =(int(input(f"Digite um valor para a posição {c}: ")))
    if entrada != 0:
        lista.append(entrada)
print(f"Você digitou os valores: {lista}")
print("")
print("")
print("")

for x in lista:
    if x > maior:
        maior = x
print(f"O maior valor da lista é: [{maior}], e está presenta nas posições: ", end="")
for pos, val in enumerate(lista):
    if maior == val:
        print(pos, end=", ")
print("Fim.")

menor = maior
for x in lista:
    if x < menor:
        menor = x
print(f"O menor valor da lista é: [{menor}], e está presente nas posições: ", end="")
for pos, val in enumerate(lista):
    if menor == val:
        print(pos, end=", ")
print("Fim.")
print()

print("-="*25)
print('FIM'.center(50))
print("-="*25)

