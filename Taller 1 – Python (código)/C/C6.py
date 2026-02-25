import cv2
import matplotlib.pyplot as plt
import numpy as np

#Leer la imagen
imagen = cv2.imread("imagen_logos.jpg")

#Convertir de BGR a RGB (para mostrar con matplotlib)
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

#Convertir a escala de grises
gris = cv2.cvtColor(imagen_rgb, cv2.COLOR_BGR2GRAY)

# Detección de bordes
bordes = cv2.Canny(gris, 50, 150)

# Obtener posiciones donde hay borde (valor distinto de 0)
coordenadas = np.column_stack(np.where(bordes > 0))
print(coordenadas) # Imprimir coordenadas en consola


plt.figure(figsize=(10,6))

plt.subplot(1,3,1)
plt.imshow(imagen_rgb)
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(gris, cmap="gray")
plt.title("Escala de Grises")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(bordes, cmap="gray")
plt.title("Bordes")
plt.axis("off")


plt.show()