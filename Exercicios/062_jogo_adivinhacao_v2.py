from random import randint
numero_pc = randint(0,10)
tentativas = 1
print("-="*30)
print(f"JOGO DA ADIVINHAÇÃO".center(60))
print("-="*30)

print("Sou seu computador...")
print("Acabei de pensar em um numero de 0 a 10")
numero = int(input("em qual numero eu pensei: "))
while numero != numero_pc:
    if numero > numero_pc:
        print("Menos, tente novamente.")
    if numero < numero_pc:
        print("Mais, tente novamente.")
    tentativas += 1
    numero = int(input("em qual numero eu pensei: "))
print(f"Voce acertou com {tentativas} tentativas.")

