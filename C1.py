import numpy as np
import matplotlib.pyplot as plt

R0 = 100
alpha = 0.00385

T = np.linspace(-200, 200, 400)
R = R0 * (1 + alpha * T)

plt.figure()
plt.plot(T, R)
plt.title("Comportamiento Sensor PT100")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ohm)")
plt.grid()
plt.show()
