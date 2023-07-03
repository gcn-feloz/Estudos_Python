numero = ('zero','um','Dois','Três','quatro','cinco',
'seis','sete','oito','nove','dez','onze','doze',
'treze','catorze','quinze','dezesseis','dezessete',
'dezoito','dezenove','vinte')
entrada = ''

print("-="*25)
print("Números por Extenso".center(50))
print("-="*25)

def valida_int(dados):
    try:
        int(dados)
        return True
    except ValueError:
        return False

def seleciona_num():
    global entrada
    while True:
        entrada = input('Digite um número de [0] até [20] ou um [número negativo] para sair: ')
        if valida_int(entrada) and (-1 < int(entrada) < 21):
            print(f"Você digitou o numero {numero[int(entrada)]}")
        elif int(entrada) < 0:
            break

seleciona_num()

print("-="*25)
print("FIM DO PROGRAMA - encerrando...".center(50))
print("-="*25)
