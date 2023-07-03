
while True:
    numero = int(input("Digite um numero para ver sua tabuada: "))
    multiplicador = int(input("Multiplicar até: "))
    if numero == 0:
        break
    for x in range(0,multiplicador+1):
        print(f"{numero} X {x:2} = {numero*x}")

    