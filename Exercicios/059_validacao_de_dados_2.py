
entrada = 1
# Mesmo que digite uma opção invalida ou mesmo somente espaços em branco ou
# somente o enter, nao vai dar erro.
print("[1] - opção 1")
print("[2] - opção 2")
print("[3] - opção 3")
print("[4] - opção 4")
print("[0] - Sair")
while entrada != '0':
    print("1")
    while ((entrada not in ['1','2','3','4']) and (entrada != '0')): # Se na entrada nao tem os numeros entao é TRUE, Entrada é diferente de zero entao é TRUE, se qualquer um der falso, ele da falso na saida final e sai do while.
        entrada = input("Digite uma opção:")    
    if entrada != '0':
        print(f"Opção valida selecionada: [{entrada}]")
        entrada = 'a'
    
    print("2")

#Nesse exemplo, ele considera não somente o primeiro caractere da entrada,
# mas a entrada inteira, durante a comparação, por isso, devem ser exatamente
# os mesmos valores durante a comparação, para que sinalize !TRUE