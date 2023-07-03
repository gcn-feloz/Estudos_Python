from moeda import metade, dobro, acrescimo


def valida_num(num):
    try:
        float(num)
        return True
    except ValueError:
        print("Digite um preço válido.")
        return False


while True:
    entrada = input("Digite o preço, ou [↩️] Enter vazio para sair: R$")
    if entrada in "":
        break
    if valida_num(entrada):
        num = float(entrada)
        print('-'*25)
        print(f"O valor digitado foi: [R${num:.2f}]")
        print()
        print(f"Metade do valor de [R${num:.2f}], é [R${metade(num):.2f}]")
        print()
        print(f"O dobro do valor de [R${num:.2f}], é [R${dobro(num):.2f}]")
        print()
        print(f"O valor [R${num:.2f}], com acrescimo de 10% é: [R${acrescimo(num):.2f}]")
        print()