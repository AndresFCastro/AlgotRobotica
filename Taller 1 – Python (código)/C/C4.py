import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Coordenadas
x = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))
z = float(input("Ingrese Z: "))

figura = plt.figure() #Colocar la ventana de la figura
ax = figura.add_subplot(111, projection='3d') # Se configura a un plano 3D

# Dibujar vector
ax.quiver(0, 0, 0, x, y, z) # Puntos iniciales en 0 y se traslada


# Dibujar punto en el vector
ax.scatter(x, y, z, color='red', s=50)


# Ajustar límites
max_val = max(x, y, z)  #Tomar valor maximo entre x,y y z
ax.set_xlim([0, (max_val+1)])
ax.set_ylim([0, (max_val+1)])
ax.set_zlim([0, (max_val+1)])


#Configuración de grafica
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Vector en Sistema 3D")
plt.show()