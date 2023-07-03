from random import randrange
nomes = []
novo = ""
while 1:

    print('Os nomes a serem sorteados são:')
    print(("inicio da lista").center(40,"-"))
    
    for nome_atual in nomes:
        print(nome_atual)   

    print(("fim da lista").center(40,"-"), end="\n")
    print("para sortear digite 'S', para sair, apenas pressione enter", end="\n")
    
    novo = input('Adicione um novo nome na lista:')
    print('\n\n\n')

    if novo == "S":
        print(' NOME SORTEADO '.center(40,"-"))
        print(' {} '.format(nomes[randrange(0,nomes.__len__()-1)]).center(40, "-"))
        print(' PARABÉNS '.center(40,"-"), end="\n\n")
        break
    elif novo:
        nomes.append(novo)
    else:
        break

        

    

    
