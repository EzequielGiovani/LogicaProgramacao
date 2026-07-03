idade = int(input(f"Digite sua idade: "))

def maior_ou_menor_idade():
    print(idade)
    if idade >= 18:
        print(f"Maior de idade")
    else:
        print(f"Menos de idade")

maior_ou_menor_idade()