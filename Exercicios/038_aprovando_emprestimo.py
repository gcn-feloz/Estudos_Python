valor_casa = float(input("Digite o valor da casa: R$"))
salario_comprador = float(input("Digite o salário do comprador: R$"))
anos = int(input("Financiar em quantos anos?: "))
prestação = valor_casa/(anos*12)
print(prestação)


print(f"Para pagar uma casa de R${valor_casa:.2f}, em {anos},")
print(f"a prestação será de apenas R${prestação:.2f}")

if prestação > (salario_comprador*.3):
    print("Emprestimo negado")
else:
    print("Emprestimo concedido")