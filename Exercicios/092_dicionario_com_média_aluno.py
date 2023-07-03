print("-="*25)
print("DICIONARIO COM MÉDIA DO ALUNO".center(50))
print("-="*25)

aluno = dict()

entrada = input("Nome do aluno: ")
aluno['nome'] = entrada
entrada = input(f"Média de {aluno['nome']}: ")
aluno['média'] = float(entrada)
if aluno['média'] < 5:
    aluno['situação'] = "Reprovado"
if 4 < aluno['média'] < 7:
    aluno['situação'] = "Recuperação"
if aluno['média'] > 6:
    aluno["situação"] = "Aprovado"
print("-"*25)
for key, val in aluno.items():
    print(f"{key} é igual a {val}")
print("-"*25)

print("-="*25)
print("Fim!".center(50))
print("-="*25)
