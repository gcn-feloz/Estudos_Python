saldo = 500.00

print(f"saldo disponivel: R${saldo}")

def sacar(valor):
    global saldo
    if saldo >= valor:
        print("valor sacado!")
        print("retire o dinheiro.")
        print("Obrigado!")
        saldo -= valor
        print(f"Saldo atual: R${saldo}")
    else:
        print("saque não autorizado")
        print("Saldo insuficiente")
        print(f"Saldo atual: R${saldo}")
    

sacar(float(input("Digite o valor que pretende sacar: R$")))