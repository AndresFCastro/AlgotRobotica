import matplotlib.pyplot as plt

# Letra A
plt.plot([0,1],[0,2])
plt.plot([1,2],[2,0])
plt.plot([0.5,1.5],[1,1])

# Letra N
plt.plot([3,3],[0,2])
plt.plot([3,4],[2,0])
plt.plot([4,4],[0,2])

plt.title("Nombre Dibujado")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.show()
