def cabeçalho(msg):
    print("-"*(len(msg)+10))
    print(msg.center(len(msg)+10))
    print("-"*(len(msg)+10))

def area(x,y):
    print(f"A Area do terreno {x}x{y} é de {x*y}m²")


cabeçalho("Area do terreno")
area(int(input(f"Largura (m): ")),int(input(f"Comprimento (m): ")))
