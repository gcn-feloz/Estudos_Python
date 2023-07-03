from random import randint



print("-="*25)
print("MAIOR E MENOR VALOR DA TUPLA".center(50))
print("-="*25)

tupla1 = tuple(randint(0,99) for _ in range(10))
print(tupla1)

print(f"Imprimindo 'tupla1' ordenada: {sorted(tupla1)}")
print(f"O menor valor da tupla1 é: {sorted(tupla1)[0]}")
print(f"O menor valor da tupla1 é: {sorted(tupla1)[len(tupla1)-1]}")

# usando min() e max()

print(f"min(tupla1): {min(tupla1)}")
print(f"max(tupla1): {max(tupla1)}")



print("-="*25)
print("-="*25)