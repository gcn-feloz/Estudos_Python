print("-="*58)
print(" SEQUENCIA DE FIBONACCI V1 ".center(116))
print("-="*58)

termos = int(input("Digite quantos termos quer calcular: "))

t1 = 0
t2 = 1
print("-="*58)
print(f" {t1} ▶️ {t2} ", end="")

cont = 3
while cont <= termos:
    t3 = t1 + t2
    print(f"▶️ {t3} ", end="")
    t1 = t2
    t2 = t3
    cont += 1
print("▶️  FIM")
print("-="*58)