nome = "jose santos de lima abreu alves de oliveira da silva"
print()
print()
# Fatiamento, significa selecionar com precisão
# uma determinada posição da string
# A primeira forma, é selecionando com um int, uma posição especifica:
print(f"nome[0]:                {nome[0]}")          #   j 

# No exemplo abaixo, começa a partir da posição zero, e vai até a nove:
print(f"nome[:9]:               {nome[:9]}")         #   jose sant

# Começa da décima posição e vai até o final da string:
print(f"nome[10:]:              {nome[10:]}")        #   s de lima abreu alves de oliveira da silva

# Retorna apenas da posição dez até a dezesseis:
print(f"nome[10:16]:            {nome[10:16]}")      #   s de l

# Retorna os caracteres do dez ao trinta, usando passo 2 (pulando a cada dois).
print(f"nome[10:30:2]:          {nome[10:30:2]}")    #   sd iaaruav

# Retorna a string completa, deixando em branco ele considera tudo.
print(f"nome[:]:                {nome[:]}")          #   jose santos de lima abreu alves de oliveira da silva

# Retorna a string completa, mas invertida.
print(f"nome[::-1]:             {nome[::-1]}")       #   avlis ad arievilo ed sevla uerba amil ed sotnas esoj

# Retorna apenas Os ultimos 18 caracteres e re-inverte os dados:
print(f"nome[:-18:-1][::-1]:    {nome[:-18:-1][::-1]}")      #   oliveira da silva
print(f"nome.rindex('abreu',0): {nome.rindex('abreu',0)}")

#Procura dentro de cada palavra dentro da string alguma correspondencia:
palavras = ('APRENDER', 'PROGRAMAR', 'PYTHON', 'LINGUAGEM', 'CURSO', 
'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for x in palavras:      #Percorre cada posição da string
    for y in x:         #Percorre cada caractere da string na posição do for anterior.
        if y in ['A', 'E', 'I', 'O', 'U']:      #Verifica cada caractere da string, se há correspondencia com os itens procurados.
            print(y, end=", ")                            # Se tiver correpondencia, é true, e ele entra no if.
print("Fim!")
print()
print()