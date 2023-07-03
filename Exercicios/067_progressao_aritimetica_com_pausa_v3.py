primeiro_termo = int()
termos = int(10)
pa = int()
lista = []

print("-="*60)
print( "PROGRESSÃO ARITIMETICA COM PAUSA" )
print("-="*60)

def verifica_int(dados):
    try:
        int(dados)
        return True
    except ValueError:
        return False

def define_pa():
    global razao, primeiro_termo
    while True:
        entrada = input("Digite o Primeiro Termo: ")
        if verifica_int(entrada):
            primeiro_termo = int(entrada)
            break
    while True:
        entrada = input("Digite a Razão da PA: ")
        if verifica_int(entrada):
            razao = int(entrada)
            break

def define_termos():
    global termos
    while True:
        entrada = input("Quantos termos a mais vc quer calcular? ")
        if verifica_int(entrada):
            termos = int(entrada)
            break




def calcula_pa():
    global pa
    while True:
        print(pa, end=" ▶️ ")
        for x in range(0,termos):
            lista.append(pa)
            pa += razao            
            print(pa, end=" ▶️ ")
        print("Pausa")
        break


define_pa()
pa = primeiro_termo

while True:
    calcula_pa()
    define_termos()
    if termos == 0:
        break
print()
print(" ENCERRANDO ".center(60, "-"))
print(" imprimindo a lista da progressão ".center(60, "-"))
print()
print(lista)
print("-="*60)
print(f"PROGRESSÃO FINALIZADA COM um total de {len(lista)} termos".center(60))
print("-="*60)


