import numpy as np
import matplotlib.pyplot as plt

# Constantes PT100
R0 = 100
A = 3.9083e-3
B = -5.775e-7
C = -4.18e-12

# Rango de temperatura
T = np.linspace(-200, 0, 500)
T1 = np.linspace(0, 200, 200)

# Ecuación PT100
Rpositivo = R0 * (1 + A*T + B*(T**2)) #Hallar resistencia respecto a la temperatura
Rnegativo = R0 * (1 + A*T1 + B*(T1**2) + C *(T1**3)*(T1-100)) #Hallar resistencia respecto a la temperatura negativo



plt.plot( T, Rpositivo,Rnegativo)
plt.title("Funcionamiento del Sensor PT100")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ohms)")
plt.grid()
plt.show()