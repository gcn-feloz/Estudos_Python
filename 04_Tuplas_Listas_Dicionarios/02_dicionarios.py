
#   Um dicionario pode ser declaro das seguintes maneiras:
dados = dict()
dados = {}
dados = {'nome_indice':'valor'}     #   nome do indice, pe o nome dado ao rótulo que vai guardar a variavel

print(dados['nome_indice'])

dados = {'chave-0':'0000',
'chave-1':'1111',
'chave-2':'2222',
'chave-3':'3333',
'chave-4':'4444',
'chave-5':'5555'
}
print()

print(dados.values())   #   exibe os valores do dicionario
print(dados.keys())     #   exibe as chaves do dicionario
print(dados.items())    #   exibe as chaves e os valores
print()
#   Imprimindo todos os itens usando o comando for
for x, y in dados.items(): 
    print(f'Imprimindo o indice: {x}. E o valor: {y}')
print()

#   Imprimindo todas as chaves usando o comando for
for x in dados.keys():
    print(f"Imprimindo as chaves: {x}")
print()

#   Imprimindo todos os valores usando o comando for
for x in dados.values():
    print(f"Imprimindo os valores: {x}")


#Para adicionar os valores dentro de um dicionario, é necessario usar ao inves do comando append(), 
# tem que ser usado o comando 'dicionario'.copy().
# o metodo .copy(), Salva uma copia do dicionario, em outra dicionario, ou dentro de uma lista ou tupla.




print()