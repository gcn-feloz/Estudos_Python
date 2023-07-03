from random import shuffle

lista = []
item = ''

while 1:
    for x in lista:
        print(x)
    print()

    item = input("Digite os [nomes] da lista ou [Enter] para sortear nova ordem ou [s] para sair:")
    if item == 's':
       break
    elif item == "":
        shuffle(lista)
    else:
        lista.append(item)
    

