print()
largura = float(input('Digite a largura da parede:'))
altura = float(input("Digite a altura da parede:"))
print()
print('Largura da parede: {:.2f} metros.'.format(largura))
print('Altura da parede: {:.2f} metros.'.format(altura))
print('A area da parede é: {:.2f} m²'.format(largura*altura))
print('Para pintar a parede é necessário {:.2f} Litros de tinta'.format((largura*altura)/9))
print()