print(" LOJAS TABAJARA ".center(60, "="))
valor = float(input("Informe o valor total da compra: R$"))

print("""
FORMAS DE PAGAMENTO:
[1] à vista - dinheiro ou cheque
[2] à vista - cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
[0] sair""")

opcao = int(input("Qual a forma de pagamento? "))


if opcao == 0:
    print("Saindo...")
elif opcao == 1:
    print("opção 1 - a vista no dinheirou ou cheque")
    print("10% de desconto:")
    print(f"O valor final da compra fica: R${(1-0.1)*valor:.2f}")
elif opcao == 2:
    print("opção 2 - à vista no cartão")
    print("5% de desconto")
    print(f"O valor final da compra fica R${(1-.05)*valor:.2f}")
elif opcao == 3:
    print("opção 3 - 2x no cartão")
    print(f"O valor final da compra fica: R${valor}")
elif opcao == 4:
    print("opção 4 - 3x ou mais no cartão")
    print(f"Acréscimo de 20% de juros")
    print(f"O valor final da compra vai ficar: R${1.2*valor}")
    parcelas = int(input("Digite em quantas vezes deseja parcelar: "))
    print(f"Sua compra será parcelada em {parcelas}X")
    print(f"E o valor de cada parcela será de: R${(valor*1.2)/parcelas}")
