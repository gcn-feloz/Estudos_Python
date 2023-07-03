#Procurar se tem Silva no nome.
nome = input("Digite o nome: ").upper().strip()
procura = input("Digite o nome pra procurar: ").upper().strip()
print(f'{nome}.')

if procura in nome:
    print(f"A palavra procurada '{procura}', foi encontrada no nome '{nome}'")
else:
    print(f"A palavra procurada '{procura}', NÃO foi encontrada no nome '{nome}'")