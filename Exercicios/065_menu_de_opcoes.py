entrada = str()
num1 = int()
num2 = int()
menu_escolhido = int()

#   VALIDA FLOAT
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
#   VALIDA INT
def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def define_numeros_calculo():
    global num1, num2
    while True:
        entrada = input("Digite o primeiro número: ")
        if is_float(entrada):
            num1 = float(entrada)
            break
    while True:
        entrada = input("Digite o segundo número: ")
        if is_float(entrada):
            num2 = float(entrada)
            break

def soma(num1, num2):
    return num1 + num2

def multiplicar(num1, num2):
    return num1 * num2

def maior(num1, num2):
    if num1 > num2:
        print(f"O número {num1} é maior que {num2}")
    elif num2 > num1:
        print(f"O número {num2} é maior que {num1}")
    elif num1 == num2:
        print(f"Os números {num2} e {num1} são iguais.") 

def seleciona_menu():
    global menu_escolhido
    while True:
        entrada = input("Digite uma opção do menu: ")
        if is_int(entrada):
            menu_escolhido = int(entrada) 
            break


def executa_operacao():
    if menu_escolhido == 1:
        print(f"A soma dos numero é:")
        print(f"{num1} + {num2} = {soma(num1, num2)}")
    if menu_escolhido == 2:
        print(f"A multiplicação dos numeros é:")
        print(f"{num1} X {num2} = {multiplicar(num1,num2)}")
    if menu_escolhido == 3:
        maior(num1, num2)
    if menu_escolhido == 4:
        define_numeros_calculo()

print("-="*30)
print("MENU DE OPÇÕES v2".center(60))
print("-="*30)


define_numeros_calculo()
while menu_escolhido != 5:

    print("""
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa
""")
    print()
    seleciona_menu()
    executa_operacao()
print("Fim do programa! Obrigado e volte sempre!")