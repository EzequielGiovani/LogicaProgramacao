#CALCULAR SAlÁRIO

def calculo_salario_original():
    salario_hora = int(input(f"Digite quando você ganha por hora: "))
    horas_p_mes = int(input(f"Digite quantas horas você trabalha por mês: "))
    salario_mes = salario_hora * horas_p_mes
    return salario_mes

salario_original = calculo_salario_original()


def calculo_bonus():
    if salario_original < 2000:
        calcular_bonus = 0
    elif salario_original >= 2000 and salario_original < 5000:
        calcular_bonus = salario_original * 0.1
    else:
        calcular_bonus = salario_original * 0.2
    return calcular_bonus
    
bonus = calculo_bonus()

def salario_final():
    salario_final = salario_original + bonus
    return salario_final

salario = salario_final()

print(f"Seu salário original é de: {salario_original:.2f}")
print(f"Seu bônus é de: {bonus:.2f}")
print(f"Seu salário final é de: {salario:.2f}")