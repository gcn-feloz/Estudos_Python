

def leiaInt(txt):
    while True:
        try:
            return int(input(txt))
        except ValueError:
            print("ERRO! Digite um número inteiro válido.") 


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")