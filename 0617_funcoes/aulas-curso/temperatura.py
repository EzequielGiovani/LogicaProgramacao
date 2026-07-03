def fahrenheit_para_celsius(f):
    """Converte teperatura de Farenheit para Celsius"""
    celsius = (f - 32) * 5 / 9
    return celsius

temp = 98
celsius = fahrenheit_para_celsius(temp)
print(celsius)