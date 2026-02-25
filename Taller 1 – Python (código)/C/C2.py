import matplotlib.pyplot as plt
from scipy import signal

print("Armemos una función de transferencia de segundo orden")
print("G(s)=(1)/(as^2+bs+c)")

# Ingreso de coeficientes
a = float(input("Ingrese coeficiente a: "))
b = float(input("Ingrese coeficiente b: "))
c = float(input("Ingrese coeficiente c: "))

# Identificación de la respúesta del sistema por medio del delta
delta = b**2 - 4*a*c

if delta > 0:
    print("Sistema Sobreamortiguado")
elif delta == 0:
    print("Sistema Críticamente Amortiguado")
else:
    print("Sistema Subamortiguado")

# Función de transferencia
num = [1]
den = [a, b, c]
system = signal.TransferFunction(num, den)

# Respuesta al escalón
t, y = signal.step(system)  # Usamos la libreria Scipy para someter el sistema a un escalon y compramos con respecto al tiempo

plt.plot(t, y)
plt.title("Respuesta Sistema de Segundo Orden")
plt.xlabel("Tiempo")
plt.ylabel("Salida")
plt.grid()
plt.show()
