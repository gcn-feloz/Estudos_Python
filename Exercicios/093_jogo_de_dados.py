from random import randint, uniform
from time import sleep

jogadas = dict()
ranking = dict()
c = int()

entrada = int(input("Quantos jogadores são? "))

print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print()
for x in range(entrada):
    print(f"Jogador {x} jogou os dados... ")
    sleep(uniform(.3,.7))
    jogadas[f'jogador {x:^3}']= randint(1,6)
    print(f"tirou: {jogadas[f'jogador {x:^3}']}")
    sleep(uniform(0.1,.3))
sleep(1)

for dado in range(6,0,-1):
    for key, val, in jogadas.items():
        if val == dado:
            c += 1
            ranking[f'{c:^3}º lugar'] = f'{key} com {val}'
            
print('-='*15)
print('RANKING DOS JOGADORES'.center(30))
print('-='*15)

for key, val in ranking.items():
    print(f"{key}: {val}")
    sleep(.35)








