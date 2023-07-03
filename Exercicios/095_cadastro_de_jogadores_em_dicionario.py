
print("-="*25)
print("CADASTRO DE JOGADORES".center(50))
print("-="*25)

jogadores = list()
gols = [5,6,1,4,8,9,2]
cadastro = dict()
entrada = str()

while True:
    cadastro.clear()
    gols.clear()
    cadastro['nome']=input("Nome: ")
    entrada = int(input(f"Quantas partidas {cadastro['nome']} jogou? "))
    cadastro['total'] = 0
    for x in range(entrada):
        gols.append(int(input(f"Quantos gols na partida {x+1}?")))
        cadastro['total'] += gols[x]
    cadastro['partida'] = gols[:]
    jogadores.append(cadastro.copy())
    entrada = input("Novo cadastro? [S/N]: ")
    if entrada in ['n','N']:
        break
print()
print("-"*20)
print("Imprindo cadastros:")
print("-"*20)
print("Imprindo lista:")
for x in jogadores:
    print(x)
print("-"*20)

for pos, val in enumerate(jogadores):
    print(f"O {pos+1}º Jogador é: {val['nome']}, jogou {len(val['partida'])} partidas, e fez um total de {val['total']} gols ")
    for pos, val in enumerate(val['partida']):
        print(f"Na {pos+1}º partida, fez {val} gols.")




print("-="*25)
print("Fim!")
print("-="*25)