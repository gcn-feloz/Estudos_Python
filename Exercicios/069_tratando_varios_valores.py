print("-="*50)
print("TRATANDO VARIOS VALORES V1".center(100))
print("-="*50)

numero = []
soma = int()
entrada = str()

def verifica_int(entrada):
    try:
        int(entrada)
        return True
    except ValueError:
        return False

def seleciona_numero():
    global entrada, numero
    while True:
        entrada = input(f"Digite {len(numero)+1}º numero ou [999 para sair]: ")
        if verifica_int(entrada):
            if int(entrada) == 999:
                break
            numero.append(int(entrada))
            break

while True:
    if entrada == '999':
        break
    seleciona_numero()

for x in numero:
    soma += x

print(f"Voce digitou {len(numero)} e a soma entre eles foi {soma} ")
print("-="*50)
print(numero)
print("-="*50)