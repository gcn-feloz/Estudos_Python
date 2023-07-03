entrada = str()
produto = []
preço = []
mais_de_mil = 0
mais_barato = 0
total = 0
i_mais_barato =0

print("-="*25)
print("LOJA SUPER BARATÃO".center(50))
print("-="*25)

def valida_float(dados):
    try:
        float(dados)
        return True
    except ValueError:
        return False

while entrada not in ['n']:
    entrada = input("Nome do produto: ")
    produto.append(entrada)
    entrada = input("Preço: R$")
    if valida_float(entrada):
        preço.append(float(entrada))
    while True:
        entrada = input("Informar outro produto? [s/n]")
        if entrada in ['s', 'n']:
            break


print(" FIM DO PROGRAMA ".center(25, '-'))

for indice, valor in enumerate(preço):
    total += valor
    if valor > 999.99:
        mais_de_mil += 1
mais_barato = total
for indice, valor in enumerate(preço):
    if valor < mais_barato:
        mais_barato = valor
        i_mais_barato = indice


print(f"O total da compra foi: R${total:.2f}")
print(f"Temos {mais_de_mil} produtos custando mais de  R$1000.00")
print(f"O produto mais barato foi, [{produto[i_mais_barato]}]")
print(f"Que custa R${mais_barato:.2f}")