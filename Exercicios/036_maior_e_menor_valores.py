qnt = int(input("Digite a quantidade de numeros para comparar: "))
numeros = []
for x in range(0,qnt):
    numeros.append(input(f"informe o {x+1}º valor: "))
print(numeros)
numeros.sort()
print(numeros)
print(f"O menor valor digitado da lista é: {numeros[0]}")
numeros.sort(reverse=True)
print(f"O maior valor digitado da lista é: {numeros[0]}")