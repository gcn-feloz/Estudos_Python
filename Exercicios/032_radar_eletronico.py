limite = 80
multa = 7
velocidade = int(input("Qual a velocidade do carro? "))

if velocidade > limite:
    print("Multado! Voce excedeu o limite permitido de 80Km/h!")
    valor = (velocidade - limite) * multa
    print(f"Você deve pargar uma multa de R${valor:.2f}!")
else:
    print("Tenha um bom dia! Dirija com segurança!")