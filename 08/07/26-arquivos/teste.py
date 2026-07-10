nomes = []

for nome in range(3):
    nome = input(f"Digite um nome: ")
    nomes.append(nome + "\n")
    with open("nomes.txt", "w") as f:
        f.writelines(nomes)

print(nomes)