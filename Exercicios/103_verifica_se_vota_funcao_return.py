import datetime
 
def cabeçalho(txt,sep='-'):
    print(sep*(len(txt)+10))
    print(txt.center(len(txt)+10))
    print(sep*(len(txt)+10))

def valida_ano(a):
    try:
        int(a)
        if int(a) < datetime.date.today().year:
            return True
        else:
            return False
    except ValueError:
        return False

def verifica_eleitor(a):
    idade = (datetime.date.today().year - a)
    if idade < 16:
        return f"Com {idade} anos: [NÃO VOTA]"
    elif 15 < idade < 18:
        return f"Com {idade} anos: [VOTO FACULTATIVO]"
    elif 17 < idade < 65:
        return f"Com {idade} anos: [VOTO OBRIGATÓRIO]"
    elif idade > 64:
        return f"Com {idade} anos: [VOTO FACULTATIVO]"

cabeçalho("Verifica se o Eleitor Vota")
while True:
    entrada = int(input("Digite o ano de nascimento: "))
    if valida_ano(entrada):
        ano_nascimento = int(entrada)
        print(verifica_eleitor(ano_nascimento))
    

    entrada = input("Continuar? [s/n]")
    if entrada in 'nN':
        break