print()
while 1:
    num =[]
    numero = input("Digite um numero de 1 até 9999, ou 0 para sair:")

    for x in range(0,len(numero)):
        num.append(numero[x])
    
    if int(numero) == 0:
        break

    elif int(numero) < 10000:
        print(''.center(50, '-'))
        print(f" O numero informado foi: {numero} ".center(50, '-'))
        
        if len(num) < 2:
            print('entrou no if')
            num.insert(0,0)
        if len(num) < 3:
            num.insert(0,0)
        if len(num) < 4:
            num.insert(0,0)

        print(f"O numero tem {len(num)} indices")
        print(num)
                        
        print(f"Unidades: {num[:-5:-1][0]}")
        print(f"Dezenas: {num[:-5:-1][1]}")
        print(f"Centenas: {num[:-5:-1][2]}" )
        print(f"Milhares: {num[:-5:-1][3]}")
    
        print(''.center(50,'-'))
print()


## OUTRA SOLUÇÃO PARA O MESMO PROBLEMA

num2 = int(input('informa um número:'))
u = num2 // 1 % 10
d = num2 // 10 % 10
c = num2 // 100 % 10
m = num2 // 1000 % 10
print(f"analisando o numero {num2}")
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

