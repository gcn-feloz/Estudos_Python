nome = "José Lima"

# também pode ser utilizado com aspas simples.
mensagem = f"""
      olá, meu nome é {nome}
   Esta é uma mensagem
            e tem recuos diferentes.
"""

print(mensagem)

# É utilizado para fazer strings, considerando nova linha,
# tabulação e espaços vazio. É util para uma quantidade grande de texto.
# permite a inclusao de variaveis.

mensagem2 = f"""
============== menu ==============
opção - 1
opção - 2
opção - 3
opção - 4
opção - 5
sair - 0
==================================
"""

print(mensagem2)