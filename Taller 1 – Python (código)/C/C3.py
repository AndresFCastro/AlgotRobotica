import numpy as np
import matplotlib.pyplot as plt

# Datos
V = float(input("Ingrese valor de Voltaje (V): "))
R = float(input("Ingrese valor de Resistencia (Ohms): "))
C = float(input("Ingrese valor de Capacitancia (uF): ")) * 1e-6  #Micro

t = np.linspace(0, 5*R*C, 500) #Intervalo de tiempo

# Carga
Vc_carga = V*(1 - np.exp(-t/(R*C))) #Ecuacion de carga

# Descarga
Vc_descarga = V*np.exp(-t/(R*C)) #Ecuación de descarga

# Gráfica
plt.plot(t, Vc_carga, label="Carga")
plt.plot(t, Vc_descarga, label="Descarga")
plt.title("Circuito RC Carga - Descarga")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.legend()
plt.grid()
plt.show()
