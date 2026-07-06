#CALCULAR MÉDIA

#sem usar listas

""" nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(media)

calcular_media(nota1, nota2, nota3)
 """


#usando listas

notas = []

quantidade = int(input(f"Quantas notas você quer informar? "))

for i in range(quantidade):
    nota = float(input(f"Digite a {i + 1} nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"A média das notas é {media}")