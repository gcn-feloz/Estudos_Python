print("-="*25)
print("BANCO MEU".center(50))
print("-="*25)

entrada = str()
valor_saque = int()
valor_sacado = 0

def valida_int(dados):
    try:
        int(dados)
        return True
    except ValueError:
        return False

def define_valor_saque():
    global valor_saque
    while True:
        entrada = input("Digite o valor que deseja sacar: R$")
        if valida_int(entrada):
            valor_saque = int(entrada)
            break

def saca_valor():
    global valor_saque, valor_sacado
    print()
    if valor_saque > 600:
        print("-"*25)
        valor_sacado = ((valor_saque*(80/100))//200)*200
        valor_saque -= valor_sacado
        print(f"Valor sacado: {valor_sacado}")
        print(f"{valor_sacado/200} x [NOTA 200]")    
        print(f"Restou R${valor_saque}")
    if valor_saque > 249:
        print("-"*25)
        valor_sacado = ((valor_saque*(60/100))//100)*100
        valor_saque -= valor_sacado
        print(f"Valor sacado: {valor_sacado}")
        print(f"{valor_sacado/100} x [NOTA 100]")
        print(f"Restou R${valor_saque}")
    if valor_saque > 124:
        print("-"*25)
        valor_sacado = ((valor_saque*(60/100))//50)*50
        valor_saque -= valor_sacado
        print(f"Valor sacado: {valor_sacado}")
        print(f"{valor_sacado/50} x [NOTA 50]")
        print(f"Restou R${valor_saque}")    
    if valor_saque > 49:
        print("-"*25)
        valor_sacado = ((valor_saque*(60/100))//20)*20
        valor_saque -= valor_sacado
        print(f"Valor sacado: {valor_sacado}")
        print(f"{valor_sacado/20} x [NOTA 20]")
        print(f"Restou R${valor_saque}")    
    if valor_saque > 24:
        print("-"*25)
        valor_sacado = ((valor_saque*(60/100))//10)*10
        valor_saque -= valor_sacado
        print(f"Valor sacado: {valor_sacado}")
        print(f"{valor_sacado/10} x [NOTA 10]")
        print(f"Restou R${valor_saque}")    
    if valor_saque > 12:
        print("-"*25)
        valor_sacado = ((valor_saque*(60/100))//5)*5
        valor_saque -= valor_sacado
        print(f"Valor sacado: {valor_sacado}")
        print(f"{valor_sacado/5} x [NOTA 5]")
        print(f"Restou R${valor_saque}")    
    if valor_saque > 1:
        print("-"*25)
        valor_sacado = ((valor_saque*(100/100))//2)*2
        valor_saque -= valor_sacado
        print(f"Valor sacado: {valor_sacado}")
        print(f"{valor_sacado/2} x [NOTA 2]")
        print(f"Restou R${valor_saque}")

define_valor_saque()
saca_valor()










print("-="*25)
print("-="*25)
