from random import randint, uniform
from time import sleep

print("-="*25)
print("GERADOR DE JOGOS PARA MEGA-SENA".center(50))
print("-="*25)

jogos = []
y = int()

entrada = int(input("Digite a quantidade de jogos que quer gerar: "))

for x in range(entrada):
    numeros = []
    y = 6
    while y > 0:
        num = randint(1,60)
        if num not in numeros:
            numeros.append(num)
            y -= 1
    jogos.append(numeros)

print("-"*50)
print(f"Gerando {entrada} jogos:")
print("-"*50)

for pos, val in enumerate(jogos):
    print(f"Jogo {pos+1}: {sorted(val)}")
    sleep(uniform(0,0.5))

print()
print(jogos)























print("-="*25)
print("Fim")
print("-="*25)