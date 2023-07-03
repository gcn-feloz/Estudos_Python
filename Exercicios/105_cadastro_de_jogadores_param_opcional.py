
jogador = {}

def cabeçalho(txt,sep='-'):
    print(sep*(len(txt)+10))
    print(txt.center(len(txt)+10))
    print(sep*(len(txt)+10))

def cadastra_jogador(n='<Desconhecido>', g=0):
    global jogador
    jogador['nome'] = n
    jogador['gols'] = g

def exibe_cadastro():
    print(f"O jogador {jogador['nome']}, fez {jogador['gols']} gol(s), no campeonato")

def recebe_dados():
    nome = input("Nome do Jogador: ")
    gols =  input("Número de gols: ")
    return nome, gols

def valida():
    if (a == "") and (b == ""):
        cadastra_jogador()
    elif (a != "") and (b == ""):
        cadastra_jogador(a)
    elif (a == "") and (b != ""):
        cadastra_jogador(g=b)
    else:
        cadastra_jogador(a,b)

while True:
    a, b = recebe_dados()
    valida()
    exibe_cadastro()

    entrada = input("Continuar [s/n]: ")
    if entrada in 'nN':
        break