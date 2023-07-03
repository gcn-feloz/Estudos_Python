from math import radians, tan, cos, sin
print()
angulo = float(input("Digite o angulo:"))
print('O SENO do angulo {}° é: {:.6f}'.format(angulo,sin(radians(angulo))))
print('O COSSENO do angulo {}° é: {:.6f}'.format(angulo,cos(radians(angulo))))
print('A TANGENTE do angulo {}° é: {:.6f}'.format(angulo,tan(radians(angulo))))
print()
