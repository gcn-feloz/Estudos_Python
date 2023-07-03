print("-="*25)
print("BOLETIM COM LISTAS COMPOSTAS".center(50))
print("-="*25)

boletim = []
cadastro = []
entrada = str()

while entrada not in ['n','N']:
    cadastro.clear()
    entrada = input("Nome:")
    cadastro.append(entrada)
    entrada = int(input("Nota 1:"))
    cadastro.append(entrada)
    entrada = int(input("Nota 2:"))
    cadastro.append(entrada)
    boletim.append(cadastro[:])
    entrada = input("Deseja cadastrar outro aluno? [S/N]: ")

print("-="*15)
print("BOLETIM DE MÉDIAS".center(30))
print("-="*15)
print(" nº|       Nome         |Média")
print("-"*30)
for pos, val in enumerate(boletim):
    print(f"{pos+1:^3}|{val[0]:^20}|{((val[1]+val[2])/2):^3}")
print()

while entrada != 0:
    entrada = int(input("Digite o nº do aluno para exibir as nostas, ou [0] para sair: "))
    if entrada != 0 and entrada < len(boletim)+1:
        print(f"As notas de {boletim[entrada-1][0]}, são: {boletim[entrada-1][1:3]}")
        print()

print()
print("Imrpindo boletins:")
print(boletim)
print("-="*25)
print("Fim!")
print("-="*25)
