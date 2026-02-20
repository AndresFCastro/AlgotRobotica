R0 = 100  # Ohmios a 0°C
A = 3.9083e-3
B = -5.775e-7
C = -4.18e-12
resistencia = 0


T = 100  # °C

if T < 0:
    resistencia = R0 * (1 + A*T + B*(T**2) +C*(T**3)*(T-100))
else:
     resistencia = R0 * (1 + A*T + B*(T**2))

# Imprimir resultado
print("La resistencia para", T, "°C es:", round(resistencia, 4), "Ohmios")


