from datetime import date
ano_atual = date.today().year

print()
print(" Alistamento ".center(50), "-")

nascimento = int(input("Digite o ANO de Nascimento: "))

idade = ano_atual - nascimento
print(f"Quem nasceu em {nascimento}, tem {idade} anos, em {ano_atual}")

if idade < 18:
    print(f"Ainda faltam {18-idade} anos, para o alistamento militar")
    print(f"Seu alistamento será em {(18-idade)+ano_atual}.")
if idade > 18:
    print(f"Você já deveria ter se alistado à {idade-18} anos atrás.")
    print(f"O ano de seu alistamento foi: {ano_atual-(idade-18)}")
if idade == 18:
    print(f"Esse é o ano de seu alistamento")
