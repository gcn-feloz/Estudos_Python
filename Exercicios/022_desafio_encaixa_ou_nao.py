N = int(input())
A = "" 
B = ""
n = N

while(n > 0):
    n -= 1
    N = input()
    A = N.split()[0]
    B = N.split()[1]

    print(f"O tamanho e valor de A: {len(A)} | {A}")
    print(f"O tamanho e valor de B: {len(B)} | {B}")

    if ((len(A) or len(B)) == 0) or ((len(A) or len(B)) >=1001):
        print('entrou no break')
        break

    if ((A[:-((len(B))+1):-1][::-1]) == B):
        print('encaixa')
    else:
        print('nao encaixa')

# compara se o valor de B é correspondente ao final da variavel A
