print()
print("-="*30)
print("DETECTOR DE PALÍNDROMO".center(60))
print("-="*30)

palavra = input("Digite uma palavra ou texto: ").strip().upper()

palavra = palavra.replace(" ","", len(palavra))

if palavra == palavra[::-1]:
    print("As palavras SÃO UM PALÍNDROMO:")
   
else:
    print(f"As palavra NÃO SÃO PALÍNDROMOS:")
    
print(f"Normal:    {palavra}")
print(f"Invertida: {palavra[::-1]}")