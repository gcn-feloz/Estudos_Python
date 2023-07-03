entrada = input("Digite algo:")


print('O tipo primitivo do valor é:', type(entrada))
print()
print('É um identificador?', entrada.isidentifier())
print('É Alphanumerico?', entrada.isalnum())
print('É Alfabetico?', entrada.isalpha())
print('É Ascii?', entrada.isascii())
print()
print('Está capitalizada? (1ª letra maiscula)', entrada.istitle())
print('É Maiusculas?', entrada.isupper())
print('É Minusculas?', entrada.islower())
print()
print('É Númerico?', entrada.isnumeric())
print('É decimal?', entrada.isdecimal())
print()
print('É digito?', entrada.isdigit())
print('É Espaços vazios?', entrada.isspace())
print()
print('É Imprimivel?', entrada.isprintable())


print('texto texto {} texto texto {} texto texto'.format(entrada.islower(), entrada.isalpha()))