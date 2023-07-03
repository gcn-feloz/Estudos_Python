entrada = "    -.0505232    ".strip()
print()
print("-="*30)
print(f"Testando se a string é fracionada: {entrada}")
print("-="*30)
print()

#   o If abaixo primeiro verifica se existe traço, representando numeros negativos.
#   Verifica se possue '-' na string, se tiver 0 é true, e se tiver 1 mas estiver na posição 0 é true.
#   Depois verifica se possue menos de 2 pontos, se sim é true, se tiver mais que dois pontos então é False
#   E por ultimo, verifica retirando o traço (se houve) e ponto (se houver), se vai ter somente digitos numericos.
#   se for true para todas essas condições, então ele reconhece a string, contendo um numero float valido.
#   Importante lembrar, que float() = int(), mas uma variavel não permite int() = float()
#   por isso ao identificar que é um numero valido, a variavel do tipo FLOAT, é a unica que vai suportar qq formato numerico.
#   Independentemente se for numero negativo e fracionado.

if (entrada.count('-') == 0 or (entrada.count('-') == 1 and entrada.find('-') == 0)) and entrada.count('.') < 2 and entrada.count(' ') == 0 and entrada.replace('.', '').replace('-','').isnumeric():
        print(f"O número é válido: {entrada}")
        num = float(entrada)
        print(f'Convertido para float: {num}')
else:
    print(f"Não é um número valido: {entrada}")

print()
print()
