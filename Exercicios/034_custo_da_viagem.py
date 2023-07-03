distancia = int(input("Qual a distancia da sua viagem? ").strip())


if distancia <= 200:
    preço = distancia*0.5
else:
    preço = distancia*0.45

print(f"Uma viagem de {distancia}Km, terá uma passagem no valor de R${preço:.2f}")