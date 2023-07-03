frase = int()   # Define uma variavel do tipo int
frase = {}      # Define um dicionario
frase = ()      # Define uma Tupla
frase = []      # Define uma Lista
frase = ""      # Define uma string literal
frase = ''      # Define uma string literal
frase = str()   # Define uma String
##################################################

frase = "Balança, Alface, Abacaxi, Avião, Banana, Almofada, Amarelo"
print()
print(" Variavel: frase ".center(60,"-"))
print(frase.center(60))
print("".center(60, "-"))

#Para saber o tamanho dessa string
# Usa-se o comando len()
print(f'A Variavel "frase" tem {len(frase)} posições.')
print()

# Para saber o tanto de ocorrencias de um determinado caractere:
# Usa-se o comando count()
print(f"O nº de ocorrencias da letra 'A' na string 'frase' é: {frase.count('A')}")
print(f"O nº de ocorrencias da letra 'a' na string 'frase' é: {frase.count('a')}")
print(f"O nº de ocorrencias da letra 'ã' na string 'frase' é: {frase.count('ã')}")
# Para contar e fatiar ao mesmo tempo:
# Usa-se o comando count('',0,22)
print(f"O nº de ocorrencias da letra 'a' na string 'frase' fatiada de 0 a 30 é {frase.count('a',0,30)}")
print()
# Para procurar um conjunto de caracteres numa string:
# Usa-se o comando find('')     Vai Retornar a posição inicial da ocorrencia
print(f"A ocorrencia 'Avião' inicia na posição: {frase.find('Avião')}")
print()
# O comando retorna o valor '-1' para indicar que não encontrou nenhuma ocorrencia
print(f"Ocorrencia 'laranja' não encontrada: {frase.find('laranja')}")
print(f"Ocorrencia 'Alface' encontrada: {frase.find('Alface')}") # E retorna a posição incial da ocorrencia
print()
# Para verificar se somente há ou não a ocorrencia pesquisada:
# Usa-se o comando in
print(f"há ocorrencia 'Almofada' na string: {'Almofada' in frase}")
print(f"Não há ocorrencia 'laranja' na string: {'laranja' in frase}")
print()
# Para substituir uma parte da string
# usa-se o comando replace()
print('"frase" antes do comando replace:'.center(60))
print(frase)
print()
print("Substituir 'Abacaxi' por '############':".center(60))
print(frase.replace('Abacaxi', '############'))
print()
print('"frase" depois do comando replace():'.center(60))
print(frase)
print()
print()
# Mas nota-se que o mesmo apenas substitui na hora, mas não modifica a variavel.
# Outra observação, é que ele reposiciona os objetos, não deformando a string.
# Para que ele salve as alterações devemos fazer da seguinte forma:
# variavel = variavel.replace('','')
print('"frase" antes do comando replace:'.center(60))
print(frase)
print()
print("Substituir 'Abacaxi' por '############' e salva:".center(60))
frase = frase.replace('Abacaxi', '############')
print(frase.replace('Abacaxi', '############'))
print()
print('"frase" depois do comando replace() e salvo:'.center(60))
print(frase)
print()
print()

# Transformar uma string em lista:
# usa-se o comando split()
print(frase.split())
print(frase) #mas ao imprimir novamente, ele não transformou a variavel em lista.
#Para salvar em lista, deve-se usar um comando de atribuição "="
frase = frase.split()
print(frase)        # Exibe a variavel 'frase' convertida em lista
print(frase[3])     # Exibe o 3º item da lista.
print(frase[3][2])  # Exibe o 2º caractere do 3º item da lista.

print()
print('-'.join(frase))
print()

