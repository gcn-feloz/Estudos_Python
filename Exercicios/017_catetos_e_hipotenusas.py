print()
cateto_oposto = float(input('Digite a medida do cateto oposto:'))
cateto_adjacente = float(input('Digite a medida do cateto adjacente:'))
hipotenusa = ((cateto_oposto ** 2)+(cateto_adjacente ** 2)) ** (1/2)
print()
print('Cateto oposto: {}'.format(cateto_oposto))
print('Cateto adjacente: {}'.format(cateto_adjacente))
print()
print('{:.2f}²+{:.2f}²={:.2f}'.format(cateto_oposto,cateto_adjacente,hipotenusa))


#usando a lib math
from math import hypot
#limpa a hipotenusa
hipotenusa = hypot(cateto_oposto,cateto_adjacente)
print()
print('Cateto oposto: {}'.format(cateto_oposto))
print('Cateto adjacente: {}'.format(cateto_adjacente))
print()
print('{:.2f}²+{:.2f}²={:.2f}'.format(cateto_oposto,cateto_adjacente,hipotenusa))

