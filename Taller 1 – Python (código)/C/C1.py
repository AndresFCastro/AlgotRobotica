import numpy as np
import matplotlib.pyplot as plt

# Constantes PT100
R0 = 100
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

# Rango de temperatura
T = np.linspace(-200, 200, 400)
R = []

# Cálculo con las dos ecuaciones
for t in T:
    if t >= 0:
        Rt = R0 * (1 + A*t + B*t**2)
    else:
        Rt = R0 * (1 + A*t + B*t**2 + C*(t-100)*t**3)
    R.append(Rt)

# Gráfica
plt.plot(T, R)
plt.title("Curva Sensor PT100 (-200°C a 200°C)")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ohm)")
plt.grid()
plt.show()