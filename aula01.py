alturas = []
generos = []

for i in range(15):
    
    altura = float(input("Altura: ").replace(",", "."))
    genero = input("Gênero (M/F): ").upper()

    alturas.append(altura)
    generos.append(genero)


soma_homens = 0
qtd_homens = 0

for i in range(15):
    if generos[i] == "M":
        soma_homens += alturas[i]
        qtd_homens += 1

media_homens = soma_homens / qtd_homens if qtd_homens > 0 else 0

print("\n--- Dados armazenados ---")
for i in range(15):
    print(f"Pessoa {i+1}: Altura = {alturas[i]} | Gênero = {generos[i]}")

print(f"\nMédia da altura dos homens: {media_homens:.2f} m")
