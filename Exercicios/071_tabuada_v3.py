entrada = str()
numero = 1
vezes = int()

print("-="*50)
print("TABUADA V3".center(100))
print("-="*50)

def verifica_int(dados):
    try:
        int(dados)
        return True
    except ValueError:
        return False

def escolhe_numero():
    global numero, vezes
    while True:
        entrada = input("Digite um numero inteiro, para calcular a tabuada: ")
        if verifica_int(entrada):
            numero = int(entrada)      
            break
    if numero > 1:
        while True:
            entrada = input(f"Digite até que número o valor [{numero}] deve ser multiplicado: ")
            if verifica_int(entrada):
                vezes = int(entrada)
                break

def executa_tabuada():
    for x in range(0, vezes+1):
        print(f"{numero} X {x} = {numero*x}")

while numero > 0:
    escolhe_numero()
    if numero > 1:
        executa_tabuada()


print("-="*50)
print("ENCERRANDO PROGRAMA!".center(100))
print("-="*50)






