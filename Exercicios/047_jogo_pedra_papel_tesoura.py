from random import randint

j = ['', '✊ - PEDRA', '✋ - PAPEL', '✌️ - TESOURA']
p1 = int()
p2 = int()
jn = int()

while True:
    print("-="*25)
    print(f"JOKENPO GAME - Jogo Nº: {jn} - Placar: Vc: {p1} - Pc: {p2}".center(50))
    print("-="*25)
    print("Escolha uma opção:")
    print("""
    [1] - PEDRA     ✊
    [2] - PAPEL     ✋
    [3] - TESOURA   ✌️
    [0] - Sair
    """)

    while True:
        j1 = int(input('Escolho: '))
        if j1 > 3:

            print("Número invalido, digite novamente.")
        else:
            break
    jn += 1
    j2 = randint(1,3)

    print("-="*25)
    print(f"Você escolheu: {j[j1]}".center(50))
    print(("xX"*5).center(50))
    print(f"O PC escolheu: {j[j2]}".center(50))
    print("-="*25)

    if j1 == 0:
        break
    elif j1 == j2:
        print("Deu empate".center(50))
    elif j1 == 1:           # Jogador escolheu PEDRA
        if j2 == 2:         # PC escolheu PAPEL
            print("Você perdeu. PAPEL Ganha de PEDRA")
            p2 += 1
        elif j2 == 3:       # Pc escolheu TESOURA
            print("Você ganhou. PEDRA Ganha de TESOURA")
            p1 += 1
    elif j1 == 2:           # Jogador escolheu PAPEL
        if j2 == 1:         # PC escolheu PEDRA
            print("Você ganhou. PAPEL ganha de PEDRA")    
            p1 += 1   
        elif j2 == 3:       # PC escolheu TESOURA
            print("Você perdeu. TESOURA ganha de PAPEL")
            p2 += 1
    elif j1 == 3:           # Jogador escolheu TESOURA
        if j2 == 1:         # PC escolheu PEDRA
            print("Você perdeu. PEDRA ganha de TESOURA")
            p2 += 1
        elif j2 == 2:       # PC escolheu PAPEL
            print("Você ganhou. TESOURA ganha de PAPEL")  
            p1 += 1      
