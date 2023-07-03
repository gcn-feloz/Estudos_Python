import random
from time import sleep
import pygame
pygame.init()
pygame.mixer.music.load('..\Python\Exercicios\m2.mp3')


num = []
num_maior = int()
num_menor = int()

print("-="*30)
print("MAIOR E MENOR Nº DA SEQUENCIA".center(60))
print("-="*30)

while True:
    n = int(input("Digite a quantidade de numeros a ser gerados na lista: "))
    n2 = int(input("Digite o valor máximo que o número poderá ter: "))
    for x in range(0,n):
        num.append(random.randint(0,n2))
        print(f"Nº {x}: {num[x]}")
        pygame.mixer.music.play()
        sleep(random.uniform(0,1.0))

      
    print("processando")
    print("Os numeros da sequencia são:")
    print(num)
    for x in num:
        if x > num_maior:
            num_maior = x
    num_menor = num_maior
    for x in num: 
        if x < num_menor:
            num_menor = x

    print(f"E o maior numero da lista é: {num_maior}")
    print(f"E o menor numero da lista é: {num_menor}")