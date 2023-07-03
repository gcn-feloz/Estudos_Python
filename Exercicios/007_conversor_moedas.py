cotacao = float(input("Digite a cotação atual da moeda:"))
montante = float(input("Digite o montante disponivel para converter:"))

print('Com a cotação atual de R${:.2f}, e com um montante de R${:.2f},\n você pode comprar até U${:.2f}'.format(cotacao, montante, montante/cotacao))