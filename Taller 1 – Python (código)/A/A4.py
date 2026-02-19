R0 = 100  # Ohmios a 0°C
A = 3.9083e-3
B = -5.775e-7


temperatura = 50  # °C

def resistencia_pt100(T):
    return R0 * (1 + A*T + B*(T**2))

# Llamar la función
resistencia = resistencia_pt100(temperatura)

# Imprimir resultado
print("La resistencia para", temperatura, "°C es:", round(resistencia, 4), "Ohmios")


