import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

wn = float(input("Ingrese la frecuencia natural (wn): "))
zeta = float(input("Ingrese el coeficiente de amortiguamiento (zeta): "))

num = [wn**2]
den = [1, 2*zeta*wn, wn**2]

system = signal.TransferFunction(num, den)
t, y = signal.step(system)

plt.figure()
plt.plot(t, y)
plt.title("Respuesta al Escalon")
plt.xlabel("Tiempo (s)")
plt.ylabel("Salida")
plt.grid()
plt.show()

if zeta < 1:
    print("Sistema Subamortiguado")
elif zeta == 1:
    print("Sistema Criticamente Amortiguado")
else:
    print("Sistema Sobreamortiguado")
