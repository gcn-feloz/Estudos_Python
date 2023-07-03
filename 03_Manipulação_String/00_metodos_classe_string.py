palavra = "    EXEMplo TExto       "

# Manipulando maiuscula e minuscula.
print(palavra.upper() + '.')
print(palavra.lower() + '.')
print(palavra.title() + '.')

# Manipulando espaços vazios.

#   Retira os espaços vazios das extremidades da string
# considera antes da primeira palavra e o final da ultima palvra.
# qualquer espaço que estiver no meio do texto nao será retirado.
print(palavra.strip() + '.') 
  
#   Retira os espaços vazios do lado direito da palavra.
print(palavra.rstrip() + '.')
print(palavra)

#   Retira os espaços vazios do lado esquedo da palavra.
print(palavra.lstrip() + '.')

#   Centraliza a palavra de acordo com o numero de caracteres.
print(palavra.center(20) + '.')
#   Centraliza e insere um caractere nos espaços da centralização.
print(palavra.center(40, "#") + '.')

print(palavra.strip().title().center(40, '#'))

#   Adicionando um caractere entre cada posiçao de uma string
print('.'.join(palavra))
