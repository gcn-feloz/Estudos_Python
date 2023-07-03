#  Calcule o preço a pagar, sabendo que o carro custa
#  R$60 por dia e R$0,15 por Km rodado.

print()
dias_alugado = int(input("Quantidade de dias alugado:"))
km_rodados = float(input("Quantidade de Km rodado:"))
print()
print('O total a pagar é de: R${:.2f}'.format((dias_alugado*60)+(km_rodados*0.15)))
