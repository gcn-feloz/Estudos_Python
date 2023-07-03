import modulos.moeda
import modulos.uteis




modulos.uteis.cabeçalho("Valor da moeda",esp=35)
modulos.uteis.cabeçalho("Substituindo . por , na formatação", '~', 15)

while True:
    entrada = input("Digite um numero ou [Enter] para sair: R$")
    if entrada in "":
        break
    if modulos.uteis.valida_float(entrada):
        entrada = float(entrada)
        print()
        print(f"O valor digitado foi: {modulos.moeda.formata_brl(entrada)}")
        print(f"Metade do valor {modulos.moeda.formata_brl(entrada)}, é: {modulos.moeda.metade(entrada)}")
        print(f"O dobro do valor {modulos.moeda.formata_brl(entrada)}, é {modulos.moeda.dobro(entrada)}")
        print(f"O acrescimo de 10% no valor {modulos.moeda.formata_brl(entrada)}, é {modulos.moeda.acrescimo(entrada)}")
        print()