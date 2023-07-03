times = ('Palmeira', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 
'Corinthians', 'Internacional', 'Cruzeiro', 'São Paulo', 'Atlético Mineiro', 
'Botafogo', 'Fluminense', 'Coritiba', 'Bahia', 'Goiás', 'Guarani', 'Sport', 
'Portuguesa', 'Atlético Paranaense', 'Vitória')

lele = 'd','de','ddds','sd'

print()
print(f"Os 5 primeiros são: ", end="")
for x in range(0,5):
    print(f'{times[x]}, ', end="")
print()
print("Os 4 ultimos são: ", end="")
for x in range(len(times)-1,len(times)-5,-1):
    print(f'{times[x]}, ', end="")
print()
print()
times = sorted(times)
print("Os times em ordem Alfabética:")
print(f"{times}")
print()
print(f"O time [Santos] está na {times.index('Santos')}ª posição.")
print()
print()

