numero = int(input("Digite um numero para ver a tabuada:"))

for tabuada in range(1,11):
    print('{:2} X {:2} = {:3}'.format(numero, tabuada, numero*tabuada))