from statistics import mean

bd = []
cadastro = {}

def cabeçalho(txt,sep='-'):
    print(sep*(len(txt)+10))
    print(txt.center(len(txt)+10))
    print(sep*(len(txt)+10))

def valida_int(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def cadastro_aluno(a):
    """
    a = aluno
    """    
    bd.append({'nome':a,'media':float(), 'prova':[]})

def cadastra_nota(c,n):
    """
    c = (codigo) posição na lista
    n = (nota) Nota do aluno
    """
    bd[c]["prova"].append(n)
    bd[c]["media"] = mean(bd[c]["prova"])

def lista_cadastro():
    print(f"{'cod':^5}|{'Aluno':^21}|{'Média':^10}")
    print("-"*36)
    m = []
    for pos,val in enumerate(bd):
        print(f"{pos:^5}|{val['nome']:^21}|{val['media']:^8.2f}")
        m.append(float(val['media']))
    if len(m) == 0:
        cabeçalho(f"A média da turma é: Zero")
    else:
        mm = mean(m)
        cabeçalho(f"A média da turma é: {mm:.2f}")

def boletim(c):
    """
    C = (cod) codigo do aluno
    """
    cabeçalho(f"Boletim do(a): {bd[c]['nome']}")
    if len(bd[c]['prova']) == 0:
        print(" ALUNO SEM NOTAS CADASTRADAS ".center(40))
    else:
        for pos, val in enumerate(bd[c]["prova"]):
            print(f"Prova {pos} ------------- nota: {val}")
    cabeçalho(f"Média final:  {bd[c]['media']:.2f}",'+')


while True:
    cabeçalho("CADASTRO DE ALUNOS E NOTAS")
    lista_cadastro()
    print("-"*36)
    print("[1] - Cadastrar Aluno")    
    print("[2] - Cadastrar Nota do Aluno")
    print("[3] - Imprimir Boletim do Aluno")
    print("[↩️] - Enter vazio para sair")
    entrada = input("Escolha uma opção: ")
    if entrada in "":
        break
    elif entrada == '1':
        cadastro_aluno(input("Digite o nome do Aluno: "))
    elif entrada == '2':
        cadastra_nota(int(input("Codigo do Aluno: ")), float(input("Nota: ")))
    elif entrada == '3':        
        boletim(int(input("Digite o codigo do Aluno:")))