from time import sleep
import sys

print("-="*25)
print("Função de contagem com passo".center(50))
print("-="*25)


def contador(começo,fim,passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = -(passo)
    if começo < fim:
        while começo < fim+1:
            print(começo, end=', ')
            sys.stdout.flush()
            sleep(.3)
            começo += passo
            
    else:
        while começo > fim-1:
            print(começo, end=', ')
            sys.stdout.flush()
            sleep(.3)
            começo -= passo
            
    print("fim!")
    print()
    print()
while True:
    contador(int(input("Começo: ")), int(input("Fim: ")), int(input("Passo: ")))
    if input("Continuar? [S/N] ") in "nN":
        break








print("-"*20)
print("Fim!")
print("-"*20)