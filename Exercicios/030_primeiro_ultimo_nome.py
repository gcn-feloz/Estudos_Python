nome = input("Digite um nome:").upper().strip()
#nome = "Maria Pereira santos albuquerque".upper().strip()

print(f"Muito prazer em te conhecer {nome}!")
print(f"Seu primeiro nome é: {nome.split()[0]}")
print(f"Seu ultimo nome é: {nome.split()[len(nome.split())-1]}")