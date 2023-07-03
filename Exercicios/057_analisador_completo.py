from statistics import mean
import pygame
pygame.init()
pygame.mixer.music.load('..\Python\Exercicios\m2.mp3')

nome = []
idade = []
sexo = []
maior_idade = 0
qnt_mulheres = 0

print("-="*30)
print("analidasor de pessoas".center(60))
print("-="*30)

while True:
    p = 0
    for x in range(0, int(input("Digite a quantidade de pessoas:"))):
        p += 1
        print(f" {p}º PESSOA".center(30, "-"))
        nome.append(input("Nome: "))
        idade.append(int(input("Idade: ")))
        sexo.append(input("Sexo [M/F]: "))
    pygame.mixer.music.play()
    media_idade = mean(idade)
    print(f"A média do grupo de idade do grupo é: {media_idade:.0f}")
    
    for x in range(0,len(idade)):
        if idade[x] > maior_idade and sexo[x] == 'M':
            maior_idade = x
    print(f"O homem mais velho tem {idade[maior_idade]} anos e se chama {nome[maior_idade]}")

    for x in range(0,len(sexo)):
        if sexo[x] == 'F' and idade[x] < 20:
            qnt_mulheres +=1
    print(f"Ao todo são {qnt_mulheres} mulheres com menos de 20 anos")


