


def cabeçalho(txt,sep):
    print(sep*(len(txt)+10))
    print(txt.center(len(txt)+10))
    print(sep*(len(txt)+10))


def calcula_fatorial(numero, show=False):
    num = numero
    for x in range((numero-1),0,-1):
        if show:
            print(f"{num} x {x} =", end=" ")
        num *= x
        if show:
            print(num) 
    if not show:
        print(f"O fatorial de {numero} é: {num}")

while True:
    num = int(input("Digite um numero para calcular o fatorial: "))
    calc = bool(int(input("Ver o calculo? [0/1] ")))
    print(calc)
    calcula_fatorial(num, calc)

    entrada = input("Continuar? [s/n] ")
    if entrada in 'nN':
        break