nome = input("informe seu nome:")
sobrenome = input("Informe seu sobrenome:")
idade = input("Informe sua idade:")

print(nome, sobrenome, idade)
print(nome, sobrenome, idade, end="...\n")
print(nome, sobrenome, idade, sep="--")
print(nome, sobrenome, idade, sep="+")
print(nome, sobrenome, idade, end="!!!\n")
print(nome, sobrenome, idade, sep="#")
print(nome, sobrenome, idade, sep="99")
print(nome, sobrenome, idade, end="...\n", sep="++")


print(f"Agora temos nas variaveis: 'nome': {nome}, 'sobrenome': {sobrenome}, 'idade': {idade}")
