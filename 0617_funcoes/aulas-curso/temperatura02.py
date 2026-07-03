# A função foi definida, mas nada aconteceu ainda...
# Precisamos chamá-la!

def fahrenheit_para_celsius(f):
    """Converte teperatura de Farenheit para Celsius"""
    celsius = (f - 32) * 5 / 9
    return celsius

temp_f = 98.6 
resultado = fahrenheit_para_celsius(temp_f)
print(f"{temp_f}F equivalem a {resultado:2f}C")

# Também podemos chamar diretamente:
print(fahrenheit_para_celsius(32))      # 0.0
print(fahrenheit_para_celsius(212))     # 100.0