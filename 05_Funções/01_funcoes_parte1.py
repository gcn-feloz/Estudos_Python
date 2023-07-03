# Para criar uma função, para rotinas, atribui-se o nome da função
# e entre parenteses, atribui-se um nome para a variavel, que vai receber
# algum tipo de dados que será usado dentro da função.
# caso a função não precise receber nenhuma entrada, pode-se apenas
# abrir e fechar parentesis: 
# função com dados: def funcao(variavel_1, variavel2, var3, v4):
# função sem dados: def funcao():

def cabecalho(msg):
    print("-"*25)
    print(msg.center(25))
    print("-"*25)

def cabecalho_prop(msg):
    print("-"*(len(msg)+10))
    print(msg.center((len(msg)+10)))
    print("-"*(len(msg)+10))







#Chama a função cabeçalho()
cabecalho("FUNÇÕES - PARTE 1")
print()

#chama a função cabecalho_prop()
cabecalho_prop("AGORA O CABEÇALHO É IMPRESSO COM TAMANHO PROPORCIONAL A FRASE.")
print()




# Chama a função contador()
# O Asterisco dentro do parametro da função contador, significa "desempacotar".
# Fazendo com que, ele possa receber uma lista de numeros, com qualquer quantidade.
# Assim a função se torna mais flexivel, a ponto, de não precisar especificar,
# uma quantidade exata de parametros, uma vez que, essa entrada pode variar.
def contador(*num):
    #Quando ele receber os dados de num, ele vai criar uma tupla chamada num
    # num = ()
    print(f"Imprimindo num: {num}")
    print(f"len(num): {len(num)}")
    print()

cabecalho_prop("Função contador:")
contador(5,6,4,2,8,9,7,0)
contador(1,5,3,6)
print("Transformou as entradas em tuplas.")
#observe que a função após receber os parametros, transforma os dados numa tupla.
print() 

# Se queremos que ele receba os dados em forma de tupla, podemos apontar
# que a entrada é uma lista.
cabecalho_prop("Funçao Def recebendo uma lista")
# Basta colocar os numeros entre chaves, lembrando que, o argumento deve
# suportar receber varias variaveis. Mas ele vai armazenar a lista, dentro
# de uma tupla
print("Transformou as entradas, em UMA lista, dentro de uma Tupla:")
print("contador([5,4,8,7,2])")
contador([5,4,8,7,2])
print("Transformou as entradas, em DUAS listas, dentro de uma Tupla:")
print("contador([1,8,9,7], [5,1,9,7,3])")
contador([1,8,9,7], [5,1,9,7,3])


#   Para trabalhar com os numeros em lista dentro de uma função:
# vamos dobrar todos os valores de uma lista com uma função:
num_0 = [5,6,4,8,7,9] # Define os numeros da lista

def dobra_num(*num):
    for x in num:
        for y in x:
            print(y*2, end=", ")

cabecalho_prop("Enviando para a função a entrada em lista")
print("Vai apenas imprimir o dobro dos numeros da entrada:")
print(f"Entrada = {num_0}")
print(f"dobra_num(num_0): ", end='')
dobra_num(num_0)
print("Fim.")
print(f"dobra_num([2,3,8,4,1,6,5]): ", end='')
dobra_num([2,3,8,4,1,6,5])
print("Fim.")
print(f"dobra_num([6,4], [8,1,3]): ", end='')
dobra_num([6,4], [8,1,3])
print("Fim.")
print()


# Conceito de referencia e desempacotamento:
#   Quando passamos para uma função uma variável como parametro, ela passa
# a ser referenciada, de forma que as alterações serão feitas em ambas
# quando alguma atribuição é feita dentro da função.

def dobra_num2(*num):
    for pos, val in enumerate(num):
        for pos1, val1 in enumerate(val):
            num[pos][pos1] = val1 * 2

# Essa função def, pega cada numero da lista que recebe, e atribui a ela mesma,
# o dobro do seu proprio valor. Salvando na lista 'num', que é a variavel usada
# como parametro pela função.
# Mas 'num' agora esta vinculada diretamente com a variavel da entrada.
# Qualquer atribuição que se faça em 'num', será feita também, na variavel
# de entrada.
lista_numeros = [4,2,8,3]
cabecalho_prop("REFERENCIAS E DESEMPACOTAMENTO")
print(f"lista_numeros = {lista_numeros}")
print("Chamando função, com uma lista de numeros e imprimindo 'lista_numeros':")
print("dobra_num2(lista_numeros): ", end='')
dobra_num2(lista_numeros)
dobra_num2([2,3,5])
print(lista_numeros)





cabecalho_prop("    FIM!    ")