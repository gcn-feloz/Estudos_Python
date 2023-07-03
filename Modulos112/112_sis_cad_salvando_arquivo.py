from mod import interface, validacao

cadastros = []

arq = 'cadastro.txt'

print()
interface.verifica_arquivo(arq)

while True:
    print()
    interface.cabeçalho("CADASTRO DE PESSOAS")
    interface.menu("Sair", "Cadastrar", "Ver cadastro")
    entrada = input("digite o número da opção: ")
    if validacao.valida_int(entrada):
        entrada = int(entrada)
        if entrada == 1:
            interface.cabeçalho("NOVO CADASTRO",'+')
            interface.cad_arquivo(arq,input('Digite o nome: '), input('Digite a idade:'))

        if entrada == 2:
            interface.cabeçalho("CADASTROS:", '~', 27)
            cadastros = interface.le_arquivo(arq)
            interface.exibe_cadastros(cadastros)
            interface.linha('~', 37)

    else:
        print("Digite uma opção válida.")
    interface.linha(tam=30)
    if entrada == 0:
        break
