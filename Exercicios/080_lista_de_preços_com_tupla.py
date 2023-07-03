

lista_de_preços = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 
'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 
'Canetas', 22.30, 'Livro', 34.90)

for p, v in enumerate(lista_de_preços):
    if p % 2 == 0:
        print((str(v).ljust(30,"-")), end=(""))
    else:
        print(f"R${float(v):.2f}")