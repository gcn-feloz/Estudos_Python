salario_atual = int(input("Qual é o salário atual? "))

if salario_atual <= 1250:
    print(f"[15%] O valor do reajuste é de R${salario_atual*.15:.2f}.")
else:
    print(f"[10%] O valor do reajuste é de R${salario_atual*.10:.2f}.")

print()