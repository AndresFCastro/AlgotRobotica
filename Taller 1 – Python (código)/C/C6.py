import cv2
import matplotlib.pyplot as plt
import numpy as np

#Leer la imagen
imagen = cv2.imread("Imagen_1.jpg")
imagen1 = cv2.imread("Imagen_2.jpg")


# Detección de bordes
bordes = cv2.Canny(imagen, 50, 150)
bordes1 = cv2.Canny(imagen1, 50, 150)

#Encontrar contornos
contornos, jerarquia = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imagen, contornos, -1, (255,0,0), 2)
print("Coordenadas contornos Imagen 1: ",contornos)

contornos1, jerarquia1 = cv2.findContours(bordes1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imagen1, contornos1, -1, (0,255,0), 4)
print("Coordenadas contornos Imagen 2: ",contornos1)



#Graficamos
plt.figure(figsize=(10,6))

plt.subplot(1,2,1)
plt.imshow(imagen)
plt.title("Imagen 1")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(imagen1)
plt.title("Imagen 2")
plt.axis("off")

plt.show()