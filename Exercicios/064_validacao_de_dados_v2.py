num = str()
def verifica_numero(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

while num != 0:
    num = input("Digite uma string para saber se é um numero valido: ")
    # Exemplos de uso
    print(f"Verificando número {num}: {(verifica_numero(num))}")         # True