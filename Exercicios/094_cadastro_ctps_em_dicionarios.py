
print("-="*25)
print("CADASTRO DE CTPS".center(50))
print("-="*25)

cadastro = {}
bd = list()



while True:
    cadastro.clear()
    cadastro['nome'] = input("Nome: ")
    cadastro['idade'] = input("Idade: ")
    cadastro['ctps'] = int(input("Ctps: "))
    if cadastro['ctps'] != 0:
        cadastro['ano_contrato'] = input("Ano do contrato: ")
        cadastro['salario'] = input("Salário: ")
    bd.append(cadastro.copy())
    if input("Continuar? [s/n] ") in ['N','n']:
        break
print()

print(f"imprimindo cadastros:")
print("="*25)

for pos, val in enumerate(bd):
    print(f"Cad {pos:2} | Nome: {val['nome']:<15} Idade: {val['idade']:2}")
    print(f"Ctps: {val['ctps']} | ", end="")
    if val['ctps'] != 0:
        print(f"Ano Contrato: {val['ano_contrato']}")
        print(f"Salário: {val['salario']}")
    print("-"*25)









print("-="*25)
print("Fim!")
print("-="*25)