## Uma outra forma de validadar os dados é utilizando comparadores condicionais.
# Como o comando While faz uma verificação e depois entra no laço, é importante atribuir um valor fora da faixa de pesquisa para nao dar erro.
numero = 0
entrada = 1
print("Escolha um numero a partir de 200 até 500")

while entrada != 0:
    entrada = 1
    while (not 200 < entrada < 500 and (entrada != 0)): # Todos os numeros dentro da faixa retorna TRUE, portanto é usado NOT, para inverter esse retorno e enquanto estiver fora da faixa ele mantem no while
        entrada = int(input("Digite um numero: "))
    if entrada != 0:
        numero = entrada
        print(f"Numero válido digitado foi: {numero}")
        


