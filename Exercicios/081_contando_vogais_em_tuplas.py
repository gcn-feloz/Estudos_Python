from time import sleep
palavras = ('APRENDER', 'PROGRAMAR', 'PYTHON', 'LINGUAGEM', 'CURSO', 
'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for v in palavras:
    print(f"{len(v):2} Letras, e na palavra {v.center(15)} temos as vogais: ", end="")
    for y in v:
        if y in ['A', 'E', 'I', 'O', 'U']:
            print(y, end=" ")
           
    print()