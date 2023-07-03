
# Uma das formas de fazer validação de dados, é usando o comando WHILE com NOT IN seguido dos caracteres que se espera encontrar
# note que para funcionar, a string que vai ser verificada não pode ser nula, já deve-se atribuir um valor antes da verificação, caso contrario dará erro.
# Pode-se atribuir um valor qq usando "entrada = 'a'"
# Ou atribui um valor para "entrada" usando já o input, e dentro do while, outro input com a advertencia:
entrada = ''
while True:
    if entrada == '0':
        break
    entrada = str(input('Informe o sexo [M/F]:')).strip().upper()[0] #  Se não houve valor na variavel a ser verificada, dará erro, por isso é importante atribuir antes de entrar no while, um valor para a variavel
    if entrada == '0':
        break
    while entrada not in '1234':        #nota-se que na procura, ele vai verificar todos os caracteres dentro da string, no caso: as letras, F, f, M, m.
        entrada = str(input('Dados invalidos, por favor, Informe o sexo [M/F]:')).strip().upper()[0] #  Com a atribuição no final '[0]' ele vai selecionar somente a posição zero da string.
        if entrada == '0':
            break            
    
    sexo = entrada
    print(f"Sexo {sexo} registrado com sucesso")

# Nesse exemplo, ele considera somente o primeiro caractere da entrada 
# para verificar se vai coincidir com algum caractere individual da string, 