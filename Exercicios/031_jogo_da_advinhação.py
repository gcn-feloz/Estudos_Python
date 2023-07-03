from random import randrange, randint
from time import sleep


print(''.center(60,'-'))
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...".center(60))
print(''.center(60,'-'))
escolhido = randrange(0,10)
numero = int(input("Em que número eu pensei? "))

print("processando...")
sleep(3)
if numero == escolhido:
    print(" PARABÉNS, VC ACERTOU MISERAVI ".center(60, '+'))
else:
    print(f" ERROU, o numero escolhido foi: {escolhido} ".center(60, '+'))
print()