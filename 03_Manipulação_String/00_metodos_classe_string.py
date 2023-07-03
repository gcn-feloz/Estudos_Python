palavra = input("Digite alguma coisa:")

# Manipulando maiuscula e minuscula.
print(palavra.upper())
print(palavra.lower())
print(palavra.title())

# Manipulando espaços vazios.

#   Retira os espaços vazios das extremidades da string
# considera antes da primeira palavra e o final da ultima palvra.
# qualquer espaço que estiver no meio do texto nao será retirado.
print(palavra.strip() + '.') 

