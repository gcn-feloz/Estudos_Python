from datetime import date


ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

print(f"O atleta tem {idade} anos de idade.")

print("Classificação:")
if idade < 9:
    print("MIRIM")
if 9 <= idade < 14:
    print("INFANTIL")
if 14 <= idade < 19:
    print("JUNIOR")
if 19 <= idade < 25:
    print("SENIOR")
if 25 <= idade:
    print("MASTER")

