#import math
from math import trunc
print()
numero = float(input('Digite um numero fracionado:'))
print()
print('O numero com 6 casas após a virgula: {:.6f}'.format(numero))
print('O numero com 5 casas após a virgula: {:.5f}'.format(numero))
print('O numero com 4 casas após a virgula: {:.4f}'.format(numero))
print('O numero com 3 casas após a virgula: {:.3f}'.format(numero))
print('O numero com 2 casas após a virgula: {:.2f}'.format(numero))
print('O numero com 1 casas após a virgula: {:.1f}'.format(numero))
print('O numero com 0 casas após a virgula: {:.0f}'.format(numero))
print('numero convertido pra int(): {}'.format(int(numero)))
print('numero truncado com comando math.trunc(): {}'.format(trunc(numero)))
print()

# Usando a função int() e usar o parametro ':.0f' podemos retirar 
# o ponto e as casas decimais de um numero fracionado.
# A diferença entre usar a função int() e usar o parametro ':.0f'
# está no arredondamento:
# EX1: numero = 4.89
# int(numero) = 4
# '{:.0f}'.format(numero) = 5

# EX2: numero = 4.45
# int(numero) = 4
# '{:.0f}'.format(numero) = 4