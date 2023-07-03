print("-="*25)
print("CADASTRO DE JOGADORES".center(50))
print("-="*25)

bd = []
cadastro = {}
gols = []

def valida_int(dados):
    try:
        int(dados)
        return True
    except ValueError:
        return False


while True:
    cadastro.clear()
    gols.clear()
    cadastro['nome'] = input("Nome: ")
    cadastro['partidas'] = int(input(f"Quantas partidas {cadastro['nome']} jogou? "))
    for x in range(cadastro['partidas']):
        gols.append(int(input(f"Quantos gols na {x+1}ª partida? ")))
    cadastro['gols'] = gols[:]
    cadastro['total_gols'] = sum(cadastro['gols'])
    print(cadastro['total_gols'])
    bd.append(cadastro.copy())
    entrada = input("Cadastrar outro jogador? [S/N] ")
    if entrada in 'Nn':
        break

print('-=*20')
print(f"{'cod':<5}|{'nome':<10}|{'gols':<35}|{'total':<5}")
print("-"*65)
for pos, val in enumerate(bd):
    print(f"{pos:<5}|{val['nome']:<10}|{str(val['gols'][:]):<35}|{val['total_gols']:<5}")

while True:
    entrada = input("Digite o cod do jogador para mais detalhes ou [N] para sair: ")
    if entrada in 'nN':
        break
    if valida_int(entrada):
        entrada = int(entrada)
        print(" Estatisticas do Jogador ".center(40, '-'))
        print(f"Cod: {entrada:<3}|Jogador: {bd[entrada]['nome']:<10}|Fez um total de {bd[entrada]['total_gols']:<2} gols.")
        for pos, val in enumerate(bd[entrada]['gols']):
            print(f"No jogo {pos+1}, fez {val} gols.")



print()












print("-="*25)
print("Fim!")
print("-="*25)
