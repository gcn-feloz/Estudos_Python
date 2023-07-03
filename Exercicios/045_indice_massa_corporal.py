peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura**2)

print(f"O IMC calculado é: {imc:.2f}")
print("De acordo com o IMC, você está:")
if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25.0:
    print("No peso ideal.")
elif imc < 30.0:
    print("Em sobrepeso.")
elif imc < 40.0:
    print("Obeso")
else:
    print("Em obesidade mórbida")



