# No python existe o Interactive Help.
# help()
# Toda função pode ser consultada se colocada dentro da função help, ou simplesmente acessando
# o terminal do python>help>comando
# ou podemos tambem pedir para imprimir o __doc__ da função.
# print(print.__doc__) imprime a documentação de print()

# DOCSTRING é um manual sobre o comando, informando sobre os parametros
# e suas funcionalidades.
def funcao(x,y,z):
    """
    Essa função imprime os parametros de entrada.
    x = qualquer string.
    y = qualquer string.
    z = qualquer string.
    """
    print(x)
    print(y)
    print(z)

help(funcao)



# Funções com parametros opcionais.
# Para atribuir parametros opcionais, deve-se atribuir um valor padrão,
# para essa variavel opcional.

def somar(x, y, z=0):
    s = x+y+z
    print(f"A soma vale {s}")

somar(5,3,7)
somar(3,4)
# A função soma, retorna o resultado como esperado, com pelo menos,
# duas variaveis sendo informadas. a terceira, por ja estar com valor = 0
# como padrão, a mesma passa a ser opcional. 



# Escopo de variaveis

# Variaveis declaradas no inicio do programa, são de escopo global,
# podem ser acessadas por qualquer função.
#   Ex.:
variavel = int()


# Variaveis criadas dentro de funções, são de escopo local,
# As mesmas não podem ser acessadas fora da função.
#   ex.:
def fun():
    variavel2 = int()
    print(variavel2)

# Se houver uma chamada para a variavel2 fora da função fun() do exemplo,
# haverá um erro, pois a variavel, só pode ser manipulada, dentro da função,
# na qual foi criada.

# Atribuindo valor a variaveis de escopo global.
# a mesma deverá ser marcada como global no inicio da função, assim dessa
# forma, ela vai conseguir fazer atribuições em variaveis de escopo global.
def fun2():
    global variavel
    variavel = 2
# Se não for declarada como global, ela irá criar outra variavel, mesmo que tiver o mesmo
# nome da variavel global, porém essa será de escopo local, assim, havera no programa
# duas variaveis com o mesmo nome, porém com escopos diferente, atendendo os chamados, por
# ordem de origem, ou seja, se a chamada partir do escopo global, será escolhida a variavel
# de escopo global, caso seja partindo de um escopo local, será usado a variavel de escopo local.


#  RETORNANDO VALORES DE FUNÇÕES.

def somar_2(a,b,c=0):
    s = a+b+c
    return s

resultado = somar_2(3,4)
print(resultado)