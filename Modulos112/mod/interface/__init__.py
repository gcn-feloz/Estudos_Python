def linha(lin='-',tam=15):
    print(lin*tam)

def cabeçalho(txt, sep='-', tam=10):
    print(sep*(len(txt)+tam))
    print(txt.center(len(txt)+tam))
    print(sep*(len(txt)+tam))

def menu(*opçoes_menu):
    for pos, val in enumerate(opçoes_menu):
        print(f"[{pos}] - [{val}]")

def exibe_cadastros(cad):
    print(f"{'cod':^5}|{'Nome':^25}|{'idade':^5}")
    for pos, val in enumerate(cad):
        val = val.replace('\n','').split(';')
        print(f"{pos:^5}|{val[0]:^25}|{val[1]:^5}")

def verifica_arquivo(arq):
    try:
        with open(arq, 'r') as cadastro:
            print(f"Aquivo cadastro.txt foi encontrado.")
    except:
        with open(arq, 'w') as cadastro:
            pass
            print("Arquivo cadastro.txt não encontra. [cadastro.txt] criado com sucesso.")

def le_arquivo(arq):
    with open(arq, 'r') as cadastro:
        a = cadastro.readlines()
        if a == '':
            a = ['O cadastro está vazio.']
            return a
        else:
            return a

def cad_arquivo(arq, nome, idade,):
    with open(arq, 'a') as cadastro:
        cadastro.write(f'{nome};{idade}\n')
    print(f"Cadastro de {nome} feito com sucesso!")