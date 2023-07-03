print("-="*25)
print("ANALISE DE DADOS DO GRUPO DE PESSOAS".center(50))
print("-="*25)

entrada = str()
idade = []
sexo = []
maior_idade = int()
qnt_homens = int()
mulher_menos_20 = int()

def valida_int(dados):
    try:
        int(dados)
        return True
    except ValueError:
        return False

def cadastra_pessoa():
    while True:
        entrada = input("Idade: ")
        if valida_int(entrada):
            idade.append(int(entrada))
            break
    while True:
        entrada = input("Sexo: ")
        if entrada in ['f','m','F','M']:
            sexo.append(entrada.upper())
            break

while True:
    print("-"*50)
    print(f"Cadastre a pessoa nº{len(idade)+1}".center(50))
    print("-"*50)
    cadastra_pessoa()
    while True:
        entrada = input("Deseja cadastrar mais uma pessoa? [S/N]")        
        if entrada in ['N','n','s','S']:
            break

    if entrada in ['N','n']:
        break

print("-="*25)
for x in idade:
    if x > 17:
        maior_idade += 1
print(f"Total de pessoas com mais de 18 anos: {maior_idade}")
for x in sexo:
    if x == 'M':
        qnt_homens += 1
print(f"Ao todo temos {qnt_homens} homens cadastrados.")
for indice, valor in enumerate(sexo):
    if valor == 'F' and idade[indice] < 15:
        mulher_menos_20 += 1
print(f"E temos {mulher_menos_20} mulheres com menos de 15 anos.")
print("-="*25)