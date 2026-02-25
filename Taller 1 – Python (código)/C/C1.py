import numpy as np
import matplotlib.pyplot as plt

# Constantes PT100
R0 = 100
A = 3.9083e-3
B = -5.775e-7

# Rango de temperatura
T = np.linspace(-200, 200, 500)

# Ecuación PT100
R = R0 * (1 + A*T + B*T**2) #Hallar resistencia respecto a la temperatura


plt.plot(T, R)
plt.title("Funcionamiento del Sensor PT100")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ohms)")
plt.grid()
plt.show()