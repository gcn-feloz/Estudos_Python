from random import randint #usado para gerar aleatorios em alguns exemplos.
# TUPLAS
# São Variaveis compostas, que podem armazenar valores diferentes, 
# em diferentes posições, começando do zero, até só deus sabe...
# A principal caracterista de uma Tupla, é que ela é IMUTAVEL.
# ou seja, os valores nela contidos, são constantes, não sendo 
# permitido atribuir valores novos, durante o programa.


# Declaração

tupla1 = ('item 0', 'item 1','item 2', 'item 3', 'item 4', 'item 5', 'item 6',
'item 7','item 8', 'item 9', 'item 10', 'item 11', 'item 12')
tupla2 = 'valor 0', 'valor 1','valor 2', 'valor 3', 'valor 4', 'valor 5', 'valor 6',  'valor 7','valor 8', 'valor 9', 'valor 10', 'valor 11', 'valor 12'

print()
print("Imprimindo TUPLA1: ", end='')
print(tupla1)
print()
print("Imprimindo TUPLA2: ", end='')
print(tupla2)
print()
 
# Imprimindo uma posição especifica da Tupla: a posição 3.
print("Imprimindo uma posição especifica da Tupla: a posição 3.")
print(f"Tupla1[5]: {tupla1[5]}")
print(f"Tupla2[5]: {tupla2[5]}")
print()

print("Imprimindo uma posição especifica, na ordem invertida.")
print(f"Tupla1[-2]: {tupla1[-2]}")
print(f"Tupla2[-2]: {tupla2[-2]}")
print()

# Imprindo de uma posição até a outra posição:
# Leve em consideração, que o numero que representa a posição final da tupla,
# não será exibido
print("Imprimindo da posição [4] até [8]")
print(f"Tupla1[4:8]: {tupla1[4:8]}")
print(f"Tupla2[4:8]: {tupla2[4:8]}")
print()

# Imprimindo do começo até uma posição especifica:
# Lembrando q ele não imprime a ultima posição.
print("Imprimindo da posição [0] até [5]")
print(f"Tupla1[:5]: {tupla1[:5]}")
print(f"Tupla2[:5]: {tupla2[:5]}")
print()

# Invertendo a ordem usando número negativo:
print("Invertendo a ordem da contagem, usando numero negativo:")
print(f"Tuplas1[-3]: {tupla1[-3:]}")
print(f"Tuplas2[-3]: {tupla2[-3:]}")
print()

# Listando toda a Tupla de três formas diferentes:
# Usando o for, com a tupla como argumento
print("Imprimindo toda a Tupla1, usando for: ")
for x in tupla1:
    print(x, end=", ")
print("FIM.")
print()
# Usando For e o len() da Tupla
print("Usando For, e len() da tupla no range:")
for x in range(0, len(tupla1)):
    print(tupla1[x], end=", ")
print("FIM.")
print()
# Usando For e o enumerate()
print("Usando For e enumerate():")
for posicao, valor in enumerate(tupla1):
    print(f"Posição: {posicao:2} | Valor: {valor}")
print("Fim.")
print()

# Exibir a Tupla ordenada mas sem alterar as posições:
print("Exibir a Tupla ordenada mas sem alterar as posições:")
print(f"Imprimindo tupla1 ordenada: {sorted(tupla1)}")
print()
print(f"Imprimindo tupla1: {tupla1}" )
print()

# Para concatenar uma tupla na outra:
print("Concatenando duas tuplas em uma nova:")
nova_tupla = tupla1 + tupla2
print(nova_tupla)
print() 

# Procurar um valor dentro da tupla:
# lista.index("valor") ou tupla.index(23)
# Lembrar de inverter o uso de aspas simples e duplas.
# Se na abertura do print foi usado aspas duplas, os argumentos de comandos
# tem que ser referenciados com aspas simples e vice-versa.
print("Procurar um valor na tupla, retornando a posição com o comando index()")
print(f'tupla1.index(item 3): {tupla1.index("item 3")}')
print()
# para eliminar a ocorrencia de encerramento do programa, ao procura-lo no indice
# e não encontrar:
def valida_indice(dados):
    try:
        tupla1.index(dados)
        return True
    except ValueError:
        return False

procura = "item 44"
print(f"Procurando um item que não esta na tupla: {procura}...")
if valida_indice(procura):
    print(f'tupla1.index(procura): {tupla1.index(procura)}')
elif not valida_indice(procura):
    print("Valor não encontrado no indice.")
print()
procura = "item 10"
print(f"Procurando um item que esta na tupla: procura = {procura}...")
if valida_indice(procura):
    print(f'tupla1.index(procura): {tupla1.index(procura)}')
elif not valida_indice(procura):
    print("Valor não encontrado no indice.")
print()

# Criando uma tupla, gerando numeros em sequencia:
print("Gerando uma tupla com numeros em sequencia:")
tupla3 = tuple(x for x in range(5))
print("tupla3 = tuple([x] for x in range(5))")
print(f"Imprimindo tupla3: {tupla3}")
print()
del tupla3 #apagando a tupla3 para gera-la novamente.
# Criando uma tupla, com números aleatórios:
print("tupla3 deletada!")
print()
print("Gerando uma tupla3 com numeros aleatórios:")
print("Criando 'tupla3' novamente")
posicoes_da_tupla = 14
print(f"Número de posições da tupla: {posicoes_da_tupla}")
tupla3 = tuple(randint(0,99) for _ in range(posicoes_da_tupla))
print(f"Imprimindo a 'tupla3': {tupla3}")
print()

# Verificando os valores minimos e maximos das tuplas,
# usando os comandos min() e  max()
print("Verificando os valores Minimos e Maximos das tuplas:")
print("Valor minimo das tuplas:")
print(f"min(tupla1)= {min(tupla1)}")
print(f"min(tupla2)= {min(tupla2)}")
print(f"min(tupla3)= {min(tupla3)}")
print("Valor máximo das tuplas:")
print(f"max(tupla1)= {max(tupla1)}")
print(f"max(tupla2)= {max(tupla2)}")
print(f"max(tupla3)= {max(tupla3)}")

# Verificando minimo e maximo de uma tupla alphanumerica:
print("Criando tupla, com dez posições, contendo numeros aleatorios:")
print("tupla4 = tuple(('valor ',randint(0,99)) for _ in range(10))")
tupla4 = tuple(('valor '+str(randint(0,99)).zfill(2)) for _ in range(10))
print(f"Imprimindo tupla4: {tupla4}")
print(f"min(tupla4): {min(tupla4)}")
print(f"max(tupla4): {max(tupla4)}")
# Conclui-se que a busca se dá por ordem alfabética e depois numerica.

print()
# A tupla pode ser deletada:
del tupla1
print("A variavel 'tupla1' foi deletada!")
# após esse comando, um erro acontecerá no programa se tentar imprimir tupla1
# pois ela não existe mais.
print()