from statistics import mean

print("-="*25)
print("CADASTRO DE PESSOAS 2v".center(50))
print("-="*25)

bd = list()
cadastro = dict()
entrada = str()

def valida_int(dados):
    try:
        int(dados)
        return True
    except ValueError:
        print("Digite um número válido.")
        return False


while True:
    cadastro.clear()
    cadastro['nome'] = input("Nome: ")
    while True:
        entrada = input("Sexo [M/F]: ")
        if entrada in ['M','m','f','F']:
            cadastro['sexo'] = entrada
            break
        else:
            print("Digite M para Masculino, ou F para Feminino.")
    while True:
        entrada = input("Idade: ")
        if valida_int(entrada):
            cadastro['idade'] = int(entrada)
            break
    bd.append(cadastro.copy())
    entrada = input("Novo Cadastro? [S/N] ")
    if entrada in ['N', 'n']:
        break
print('-'*20)
print(bd)
print('-'*20)
print("ESTATISTICAS DO CADASTRO:")
print('-'*20)
print(f"[A] - Ao todo temos {len(bd)} pessoas cadastradas")
print('-'*20)
média = mean(pessoa['idade'] for pessoa in bd)
print(f"[B] - A média da idade é: {média}")
print('-'*20)
print("[C] - As Mulheres cadastradas foram: ", end="")
for mulheres in bd:
    if 'F' in mulheres['sexo']:
        print(mulheres['nome'], end=", ")
print("Fim.")
print('-'*20)
print(f"[D] - Lista das pessoas que estão acima da média de idade: ")
for acima_media in bd:
    if acima_media['idade'] > média:
        print(f"Nome: {acima_media['nome']:^10}; Sexo: {acima_media['sexo']:<2}; Idade: {acima_media['idade']:<2};")

print(f"")

'''
print('-'*20)
print("IMPRIMINDO O CADASTRO:")
print('-'*20)

'''



print("-="*25)
print("Fim!")
print("-="*25)