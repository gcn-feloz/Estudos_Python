MAIORIDADE = 18
IDADE_ESPECIAL = 14
maioridade = "o"

idade = int(input("Digite sua idade:"))

##Estruturas condicionais com IF, ELIF, ELSE
if idade >= MAIORIDADE:
    print("Já pode tirar a CNH")
elif idade >= IDADE_ESPECIAL:
    print("Já pode assistir aulas teoricas")
else:
    print("Não tem idade suficiente para aulas teoricas nem pratica.")

## Estrutura IF Ternário, um IF de uma unica linha.
status = "100%" if idade >= MAIORIDADE else "50%"
print(status)