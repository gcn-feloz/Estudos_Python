from datetime import date
ano_atual = date.today().year

anos_nascimento = []
idades = []
c = 0
de_menor = int()
de_maior = int()

while True:
    
    print("-="*30)
    print("Grupos de idades".center(60))
    print("-="*30)
    print()
    print("[0] - Sair")
    print("[1] - Classificar")
    print("OU")
    entrada = int(input(f"Digite o ano de nascimento da pessoa {c}:"))
    if entrada == 0:
        break
    elif entrada == 1:
        print("Classificação:")
        for x in range(0,len(idades)):
            print(f"A pessoa {x:2}, tem {idades[x]:2} anos, e nasceu em {anos_nascimento[x]}.")
            if idades[x] >= 18:
                de_maior +=1
            elif idades[x] < 18:
                de_menor +=1
        print(f"Tem {de_menor} pessoas de menor na lista.")
        print(f"Tem {de_maior} pessoas de maior na lista.")

    elif  entrada/1000 >= 1 and entrada < ano_atual:
        c += 1
        anos_nascimento.append(entrada)
        idades.append(ano_atual - entrada)













