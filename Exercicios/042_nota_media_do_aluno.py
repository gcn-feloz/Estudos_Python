import statistics
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = statistics.mean([nota1,nota2])
print(f"Tirando {nota1}, e {nota2}, a média do aluno é: {media}")

if media < 5.0:
    print("Reprovado")
if 5.0 <= media <= 6.9:
    print("Recuperação")
if 7.0 <= media:
    print("Aprovadasso!")