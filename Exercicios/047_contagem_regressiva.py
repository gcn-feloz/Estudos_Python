from time import sleep

contagem = int(input("Digite um numero para contagem regressiva: "))

while contagem:
    print(f"Contagem em: {contagem}")
    contagem -= 1
    sleep(1)
print("Fim da contagem!")
