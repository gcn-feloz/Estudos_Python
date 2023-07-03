numero = int(input("Digite um numero para converter:"))
print("-="*25)
print(f"O numero escolhido: {numero}".center(50))
print("-="*25)
print("""Escolha uma opção de conversão:
[1] binário
[2] octal
[3] hexadecimal""")
print("-="*25)
while True:
    a = int(input())
    if a == 1:
        print(f"BINARIO: {bin(numero)}")
    if a == 2:
        print(f"OCTAL: {oct(numero)}")
    if a == 3:
        print(f"HEXADECIMAL: {hex(numero)}")
    if a == 0:
        break
    if a > 3:
        print("Numero invalido. Digite de [1],[2],[3], ou [0] para sair.")
    