curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [32, 80, 40, 50, 15]
presente = True

#Começando pela variavel curso, mostra o tipo 
# dela que é str, e printa o conteudo.
print(f"Variavel: curso |Tipo:{type(curso)} |Conteudo:{curso}") 
#Procura na variavel Curso, qualquer sequencia que corresponda
# exatamente a sequencia de caracteres digitadas no input.
presente = input(f"Na 'str' 'curso' Procure por:") in curso
#Se estiver presente, true, se não, false
print(presente, end="\n\n")

#Analisa a lista frutas
print(f"Variavel: frutas |Tipo:{type(frutas)} |Conteudo:{frutas}")
presente = input(f"Na 'list' 'frutas', procure por:") in frutas
print(presente, end="\n\n")
presente = input(f"Na 'list' 'frutas', procure por:") not in frutas
print(presente, end="\n\n")


print(f"Variavel: saques |Tipo:{type(saques)} |Conteudo:{saques}")
presente = int(input(f"Na 'list' 'saques', procure por:")) in saques
print(presente, end="\n\n")
presente = int(input(f"Na 'list' 'saques', procure por:")) not in saques
print(presente, end="\n\n")