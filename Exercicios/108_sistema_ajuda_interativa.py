

def cabeçalho(txt,sep='-'):
    print(sep*(len(txt)+10))
    print(txt.center(len(txt)+10))
    print(sep*(len(txt)+10))




while True:

    entrada = input("digite o nome de uma função ou biblioteca ou [↩️] Enter vazio para sair.: ")
    if entrada in '':
        break
    else:
        try:
            help(entrada)
        except ValueError:
            print("Digite uma o nome de uma função ou Biblioteca válida!")