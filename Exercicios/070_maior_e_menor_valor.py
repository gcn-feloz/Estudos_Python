from statistics import mean
lista = []
entrada = "a"
maior = int()
menor = int()

print("-="*50)
print(" MAIOR E MENOR VALOR ".center(100))
print("-="*50)

def verifica_int(dados):
    try:
        int(dados)
        return True
    except ValueError:
        return False

def adiciona_numero():
    global entrada
    while True:
        entrada = input(f"Digite o {len(lista)+1}º número: ")
        if verifica_int(entrada):
            lista.append(int(entrada))    
            break

while entrada not in 'nN':
    adiciona_numero()
    while entrada not in ['n','N', 's', 'S'] :
        entrada = input(f"Adicionar outro número? [S/N]: ")

for x in lista:
    if maior < x:
        maior = x
menor = maior
for x in lista:
    if menor > x:
        menor = x

print("-="*50)
print("Finalizando o programa".center(100))
print(f"Você digitou {len(lista)} números, e a média deles é: {mean(lista):.2f}.".center(100))
print(f"O maior valor foi [{maior}], e o menor valor foi [{menor}].".center(100))
print("Imprimindo a lista...".center(100))
print("-="*50)
print(lista)
print("-="*50)
print()