while True:
    print()
    numeros = []
    n_encontrados = []
    n_multiplos = int()
    soma_n = int()

    tempin = int(input("Digite até que numero deve ser verificado multiplos de três:"))
    if tempin == 0:
        break
    for x in range(0, tempin+1):
        numeros.append(x)
    print(f"A lista gerada é: {numeros}")
    print()
    for x in numeros:
        if x % 3 == 0 and x % 2 == 1:
            print(f"Numero multiplo encontrado: {x}")
            n_encontrados.append(x)
            n_multiplos += 1
            soma_n += x

    print(f"A lista com os numeros multiplos: {n_encontrados}")
    print()
    print(f"Foram encontrados [{n_multiplos}] nº multiplos de três.")
    print(f"A soma de todos esse numeros resulta em: [{soma_n}].")
    print()
