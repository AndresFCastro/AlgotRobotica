import numpy as np
import matplotlib.pyplot as plt

V = float(input("Ingrese el voltaje (V): "))
C = float(input("Ingrese la capacitancia (uF): ")) * 1e-6
R = float(input("Ingrese la resistencia (Ohm): "))

tau = R * C
t = np.linspace(0, 5*tau, 500)

Vc_carga = V * (1 - np.exp(-t/tau))
Vc_descarga = V * np.exp(-t/tau)

plt.figure()
plt.plot(t, Vc_carga, label="Carga")
plt.plot(t, Vc_descarga, label="Descarga")
plt.title("Circuito RC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.legend()
plt.grid()
plt.show()
