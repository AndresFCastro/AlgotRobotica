import matplotlib.pyplot as plt
import numpy as np

x = [-2, -1, -1, 1, 1, 2, 2, 1, 1, -1, -1, -2, -2]
y = [0.5, 0.5, 1, 1, 0.5, 0.5, -0.5, -0.5, -1, -1, -0.5, -0.5, 0.5]

plt.plot(x, y)
plt.title("Logo Chevrolet (Aproximado)")
plt.gca().set_aspect('equal')
plt.grid()
plt.show()

t = np.linspace(0, 2*np.pi, 400)
x = 3*np.cos(t)
y = 1.5*np.sin(t)

plt.plot(x, y)
plt.title("Logo Hyundai (Aproximado)")
plt.gca().set_aspect('equal')
plt.grid()
plt.show()
