# declaração de listas:

lista1 = []
lista1 = list()
lista1 = ['valor1','valor2','valor3','valor4','valor5','valor6','valor7']

# Lista composta:

lista2 = [['valor1','valor2','valor3','valor4'], ['item1','item2','item3','item4'],
['nome1','nome2','nome3','nome4'], ['info1','info2','info3','info4']]
print()
print("Cria a lista composta:")
print("""lista2 = [['valor1','valor2','valor3','valor4'], ['item1','item2','item3','item4'],
['nome1','nome2','nome3','nome4'], ['info1','info2','info3','info4']]""")
print()
print(f"Imprimindo lista2[0]: {lista2[0]}")
print(f"Imprimindo lista2[0][0]: {lista2[0][0]}")
print(f"Imprimindo lista2[0][2]: {lista2[0][2]}")  

#   Para exibir a lista dentro da lista, de forma sequencial e com seus dados organizados
# pode-se usar um for, para percorrer a primeira lista, e somente mandar exibir as
# posições como no exemplo abaixo:

for x in lista2:
    print(f"0: {x[0]}, 2: {x[1]}, 3: {x[2]}, 4: {x[3]}")


print()
print("-"*25)
# Metodos de adição e atribuição de dados em listas:
print("Metodos de atribuição em listas:")
print("-"*25)
print("Criando lista3:")
print('lista3 = ["info 1","info 2"]') #Lembrar de inverter o uso de aspas simples e duplas, na abertura do argumento deve ser uma, e dentro do argumento deve ser a outra.
print()
lista3 = ["info 0","info 1","info 2"]
print(f"lista3 criada, imprimindo lista: {lista3}")

#Para adicionar no final da lista:
#Usa-se o metodo append()
print()
print("++  Metodo append()  ++")
lista3.append('info 3')
print(f"lista3.append('info 3'): {lista3}")
print()

#Para adicionar dados em uma lista, especificando uma posição:
#Usa-se o metodo insert(), podendo também passar a posição especifica no argumento.
# Nota-se que ele vai adicionar na posição especifica, e vai refazer a lista
# de forma que todos os dados que estão após a inserção, irão ser realocados,
# em suas respectivas posições subsequente, empurrando toda a lista para frente
print("++  Metodo insert()  ++")
lista3.insert(1, 'nova info')
print(f"lista3.insert(1, 'nova info'): {lista3}")
print()

# Usando atribuição direta com o sinal de igual, a uma posição especifica:
# Ele vai substituir os dados já existentes na posição, e vai salvar a 
# nova atribução na posição especificada
print("++  Atribução direta  ++")
lista3[2] = 'outra info'
print(f"lista3[2] = 'outra info': {lista3}")
print()



# Retirando informações da lista:
print("-"*25)
print("Retirando informações da lista")
print("-"*25)
print()
# Removendo dados referenciando pela posição.
print("++  Comando del()  ++")
del lista3[2]
print(f"del lista3[2]: {lista3}")
print()
print("++  Metodo pop()  ++")
lista3.pop(1)
print(f"lista3.pop(1): {lista3}")
print()
#Removendo dados referenciando pelos dados.
print("++  Metodo remove()  ++")
lista3.remove("info 3")
print(f'lista3.remove("info 2"): {lista3}')
print()

print()
print()

print()
# Pra dar um append() de uma lista pra armazenar em outra lista, é preciso que ela faça o fatiamento, ou seja, que percorra todas as posições.









