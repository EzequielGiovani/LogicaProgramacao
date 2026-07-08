salario_hora = int(input(f"Quanto você ganha por hora? "))
horas_p_mes = int(input(f"Quantas horas você trabalha por mês? "))
salario_original = salario_hora * horas_p_mes

def calcular_bonus():
    if salario_original < 2000:
        valor_bonus == 0
    elif salario_original > 2000 and salario_original < 5000:
        valor_bonus = salario_original * 0.1
    else:
        valor_bonus = salario_original * 0.2
    return valor_bonus

bonus = calcular_bonus()
salario_final = salario_original + bonus

print(f"Seu salário original é de: {salario_original:.2f}")
print(f"Seu bônus é de: {bonus:.2f}")
print(f"Seu salário final é de: {salario_final:.2f}")