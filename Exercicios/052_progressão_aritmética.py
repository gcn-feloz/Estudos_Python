print("="*60)
print("OS TERMOS DA UMA PA".center(60))
print("="*60)

primeiro_termo = int(input("Digite o primeiro termo da progressão: "))
razao = int(input("Digite o valor da razão da progressão: "))
qnt_termos = int(input("Digite a quantidade de termos da progressão: "))
pa = []
pa.append(primeiro_termo)
for x in range(1,qnt_termos):
    pa.append(pa[x-1]+razao)

print("Lista criada:")
print(pa)
