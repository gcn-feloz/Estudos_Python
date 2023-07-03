saldo = 450
limite = 200
saque = 20
#saque = int(input("digite o valor do saque:"))

#Comparador
print(f"saque é maior que o limite? {saque > limite}")
print(f"saque é maior que o saldo? {saque > saldo}")

#Operador E
print("Pode sacar?", saque < limite and saque < saldo, end="\n\n")

######################
print("--+#||#+-- Criando as variaveis --+#||#+--")
verdadeiro = True
falso = False
print("verdadeiro:", verdadeiro)
print("falso:", falso, end="\n\n")

#Operador !Não
print("Aplicando operador 'not' as variaveis:")
print("NOT verdadeiro:", not verdadeiro)
print("NOT falso:", not falso, end="\n\n")

#Operador E
print("Aplicando o operador AND nas variaveis:")
print("verdadeiro AND verdadeiro:", verdadeiro and verdadeiro)
print("verdadeiro AND falso:", verdadeiro and falso)
print("falso AND falso:", falso and falso, end="\n\n")

#Operador OU
print("Aplicando operador OR, nas variaveis")
print("verdadeiro OR verdadeiro:", verdadeiro or verdadeiro)
print("verdadeiro OR falso:", verdadeiro or falso)
print("falso OR falso:", falso or falso, end="\n\n")
