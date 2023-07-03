print("-="*25)
print("LISTAS COMO MATRIZES".center(50))
print("-="*25)

lista = [[],[],[]]

for x in range(3):
    for y in range(3):
        lista[x].append(int(input(f"Digite um valor para [{x}, {y}]: ")))
        

print(f"[{lista[0][0]:^5}] [{lista[0][1]:^5}] [{lista[0][2]:^5}]")

print(f"[{lista[1][0]:^5}] [{lista[1][1]:^5}] [{lista[1][2]:^5}]")

print(f"[{lista[2][0]:^5}] [{lista[2][1]:^5}] [{lista[2][2]:^5}]")












print("-="*25)
print("-="*25)