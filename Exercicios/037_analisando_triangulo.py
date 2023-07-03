print("-="*20)
print(" ANALISADOR DE TRIANGULOS".center(40))
print("-="*20)

r1 = input("Digite o 1º seguimento: ")
r2 = input("Digite o 2º seguimento: ")
r3 = input("Digite o 3º seguimento: ")

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos acima podem formar um triangulo.")
else:
    print("Os seguimentos acima não podem formar um triangulo.")