
numero = int(input("Digite um numero para verificar se é primo: "))
list_numero = []


for x in range(1,numero +1):
    if numero % x == 0:
        print('✅', end='')
        list_numero.append(x)
    else:
        print('❌', end='')
    print(x, end='-')
print()
print(f"O numero {numero}, pode ser dividido por:")
print(list_numero)

print(len(list_numero))
print(f"O numero {numero} ", end='')
if len(list_numero) < 3:
    print("É UM NUMERO PRIMO")
else:
    print("NÃO É UM NUMERO PRIMO")
    
    