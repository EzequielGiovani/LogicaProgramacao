#CALCULAR IMC

def calcular_imc():
    peso = float(input(f"Digite seu peso: "))
    altura = float(input(f"Digite sua altura: "))
    calcular = peso / (altura * altura)
    print(calcular)

calcular_imc()

#MESMO CÓDIGO, MAS USANDO return

'''
def calcular_imc():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    calcular = peso / (altura * altura)
    return calcular

imc = calcular_imc()
print(imc)
'''