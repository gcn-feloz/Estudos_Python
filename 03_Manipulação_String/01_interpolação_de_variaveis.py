nome = "José"
idade = 23
profissao = "Mecânico"
Apelido = "Engrenagem"

print("Olá, me chamo {}, tenho {} anos, trabalho como {},".format(nome, idade, profissao, ))
print("e meus colegas me apelidaram de {}.".format(Apelido))

# outra maneira de interpolar uma string é da seguinte forma:
# print(f"...{variavel}... ... .. {variavel} ... ...")
print(f"Olá, me chamo {nome}, tenho {idade} anos,")
print(f"trabalho como {profissao}, e meus colegas me apelidaram de {Apelido}.")

#   utilizando um dicionario
dados = { 'nome':'José','idade':'23','profissao':'Mecânico','Apelido':'Engrenagem'}
print("Olá, me chamo {nome}, tenho {idade} anos,".format(**dados))
print("trabalho como {profissao}, e meus colegas me apelidaram de {Apelido}.".format(**dados))

#Formantando um float dentro de uma interpolação de Strings
import math

print(f"O valor de PI é:{math.pi:.0f}")
print(f"O valor de PI é:{math.pi:.1f}")
print(f"O valor de PI é:{math.pi:.2f}")
print(f"O valor de PI é:{math.pi:.3f}")
print(f"O valor de PI é:{math.pi:.4f}")
print(f"O valor de PI é:{math.pi:.5f}")

# E adicionando caracteres antes da virgula.
print(f"O valor de PI é:{math.pi:0.5f}")
print(f"O valor de PI é:{math.pi:1.5f}")
print(f"O valor de PI é:{math.pi:2.5f}")
print(f"O valor de PI é:{math.pi:3.5f}")
print(f"O valor de PI é:{math.pi:4.5f}")
print(f"O valor de PI é:{math.pi:5.5f}")