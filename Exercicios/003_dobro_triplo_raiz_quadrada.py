#import math
from math import sqrt

entrada = int(input("Digite um numero:"))

print('O dobro de {} vale: {}.'.format(entrada, entrada*2))
print('O triplo de {}, vale: {}.'.format(entrada, entrada*3))
print('A Raiz quadrada de {}, vale {}.'.format(entrada, sqrt(entrada)))
print('A raiz quadrada de {}, vale {}.'.format(entrada, entrada ** (1/2)))