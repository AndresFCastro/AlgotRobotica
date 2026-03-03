import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

K = float(input("Ingrese la ganancia K: "))
wn = float(input("Ingrese la frecuencia natural Wn: "))
zeta = float(input("Ingrese el factor de amortiguamiento ζ: "))


numerador = [K * wn**2] #Numerador de la función 
denominador = [1, 2*zeta*wn, wn**2] #Denominador de la función

sistema = signal.TransferFunction(numerador, denominador) #Utilizamos funcion de spcipy para formar la funcion de transferencia

Ts = 4/(zeta*wn)
t = np.linspace(0, 2*Ts, 1000)


t, y = signal.step(sistema, T=t) #Sometemos el sistema a un escalon

#Identificar el tipo de respuesta
if zeta < 1:
    tipo = "Subamortiguado"
elif zeta == 1:
    tipo = "Críticamente amortiguado"
else:
    tipo = "Sobreamortiguado"

print("Tipo de sistema:", tipo)


plt.plot(t, y)
plt.title(f"Respuesta del sistema ")
plt.xlabel("Tiempo")
plt.ylabel("Salida")
plt.grid()
plt.show()