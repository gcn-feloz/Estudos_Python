

def cabeçalho(txt,linha):
    print()
    print(linha*(len(txt)+10))
    print((txt).center(len(txt)+10))
    print(linha*(len(txt)+10))
    print()


while True:
    cabeçalho(input("Digite texto do cabeçalho: "), input("Desenhar a linha com: "))
    if input("criar outro cabeçalho? [S/N]: ") in "Nn":
        break