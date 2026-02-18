import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = float(input("Ingrese coordenada X: "))
y = float(input("Ingrese coordenada Y: "))
z = float(input("Ingrese coordenada Z: "))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, x, y, z)
ax.set_xlim([0, max(1,x)])
ax.set_ylim([0, max(1,y)])
ax.set_zlim([0, max(1,z)])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Vector en 3D")

plt.show()
