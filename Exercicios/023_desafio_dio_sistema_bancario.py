import datetime


extrato = []
lançamento = {
    'horario':'','valor':'','saldo':''
}


print(f"saldo1: {extrato}")
lançamento = {'horario':datetime.datetime.now().strftime("%H:%M:%S"), 'valor': 2,'saldo': 2}
extrato.append(lançamento.copy())
for x in range(1,5):
    lançamento = {'horario':datetime.datetime.now().strftime("%H:%M:%S"), 'valor': x,'saldo': x+(extrato[x-1]['saldo'])}
    extrato.append(lançamento.copy())
    print(extrato)

print(f"""extrato""".center(40, "-"))

for x in extrato:
    print(extrato[0]['valor'])
    for a in x.values():
        print(f'{a}', end='')

'''
for x in extrato:
    for a in x.items():
        print(f'{a}')
'''


'''
valor_deposito = int(input('Digite o valor do deposito:'))
saldo += valor_deposito
extrato.append(datetime.datetime.now().strftime("%H:%M:%S"),valor_deposito, saldo)
print(extrato)
'''















