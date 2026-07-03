def calcular_media(numeros):
    if not numeros:
        return 0.0
    total = sum(numeros)
    return float(total) / len(numeros)

exemplo = [7, 8, 9, 10]
resultado = calcular_media(exemplo)
print(resultado)