frutas = ["maça", "banana", "laranja", "melão"]

  
#   for nome_do_laço in Intervalo:
# nome do laço, vira tambem uma variavel.
# Se o intervalo for uma string, ele vai 
# considerar todas as posições não vazias.

for fruta_atual in frutas:
    print(fruta_atual)
 
# Contagem progressiva

for repetição in range(0,8):
    print(repetição)
print()

# Contagem de dois em dois
for laço in range(0, 10, 2):
    print(laço)
print()

# Em contagem regressiva
for laço in range(10, 0, -1):
    print(laço)
print("fim")

# Repetição interativa
for laço in range(int(input("Inicio:")), int(input("Fim:")), int(input("Passo:"))):
    print(laço)
print("Fim.")
print()
