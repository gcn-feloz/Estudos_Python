fatorial = int()

print("-="*25)
print("Calculo do Fatorial".center(60))
print("-="*25)



def verifica_int(dados):
    try:
        int(dados)
        return True
    except ValueError:
        return False

print("")
while True:
    entrada = input("Digite um numero para calcular o fatorial: ")
    if verifica_int(entrada):
        numero = int(entrada)
        break
fatorial = 1
for x in range(numero,0,-1):
    print(f"{x} x ", end='')
    fatorial *= x
    print(fatorial)
print(f"fatorial: {fatorial}")  