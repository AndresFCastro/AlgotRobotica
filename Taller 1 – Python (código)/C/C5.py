import matplotlib.pyplot as plt
import numpy as np


#Nombre 1 - --------- FELIPE
plt.figure()

# Letra F
plt.plot([1,1], [0,5])
plt.plot([1,3], [5,5])
plt.plot([1,3], [3,3])

#Letra E
plt.plot([5,5], [0,5])
plt.plot([5,7], [5,5])
plt.plot([5,7], [3,3])
plt.plot([5,7], [0,0])

#Letra L
plt.plot([9,9], [0,5])
plt.plot([9,11], [0,0])

#Letra I
plt.plot([13,13], [0,5])

#Letra P
plt.plot([15,15], [0,5])
plt.plot([15,17], [5,5])
plt.plot([17,17], [5,3])
plt.plot([17,15], [3,3])

#Letra E
plt.plot([19,19], [0,5])
plt.plot([19,21], [5,5])
plt.plot([19,21], [3,3])
plt.plot([19,21], [0,0])

plt.title("FELIPE")
plt.axis('equal')
plt.grid()




#Nombre 2 ----------- JAVIER
plt.figure()

#Letra J
plt.plot([23,25], [5,5])
plt.plot([24,24], [5,0])
plt.plot([23,24], [0,0])

#Letra A
plt.plot([27,28], [0,5])
plt.plot([28,29], [5,0])
plt.plot([27.5,28.5], [2.5,2.5])

#Letra V
plt.plot([32,31], [0,5])
plt.plot([32,33], [0,5])
plt.plot([27.5,28.5], [2.5,2.5])

#Letra I
plt.plot([35,35], [0,5])


#Letra E
plt.plot([37,37], [0,5])
plt.plot([37,39], [5,5])
plt.plot([37,39], [3,3])
plt.plot([37,39], [0,0])

#Letra R
plt.plot([41,41], [0,5])
plt.plot([41,43], [5,5])
plt.plot([43,43], [5,3])
plt.plot([43,41], [3,3])
plt.plot([41,43], [3,0])

plt.title("JAVIER")
plt.axis('equal')
plt.grid()

#Nombre 3 ----------- ERICK
plt.figure()

# Letra E
plt.plot([1,1], [0,5])
plt.plot([1,3], [5,5])
plt.plot([1,3], [3,3])
plt.plot([1,3], [0,0])

#Letra R
plt.plot([5,5], [0,5])
plt.plot([5,7], [5,5])
plt.plot([7,7], [5,3])
plt.plot([7,5], [3,3])
plt.plot([5,7], [3,0])

#Letra I
plt.plot([9,9], [0,5])

#Letra C
plt.plot([11,11], [0,5])
plt.plot([11,13], [5,5])
plt.plot([11,13], [0,0])

#Letra K
plt.plot([15,15], [0,5])
plt.plot([15,17], [3,5])
plt.plot([15,17], [3,0])

plt.title("ERICK")
plt.axis('equal')
plt.grid()


#Nombre 4 ----------- ANDRES
plt.figure()

#Letra A
plt.plot([1,2], [0,5])
plt.plot([2,3], [5,0])
plt.plot([1.5,2.5], [2.5,2.5])

#Letra N
plt.plot([5,5], [0,5])
plt.plot([5,7], [5,0])
plt.plot([7,7], [0,5])

#Letra D
plt.plot([9,9], [0,5])
plt.plot([9,10], [5,5])
plt.plot([10,11], [5,4])
plt.plot([11,11], [4,1])
plt.plot([11,10], [1,0])
plt.plot([10,9], [0,0])

#Letra R
plt.plot([13,13], [0,5])
plt.plot([13,15], [5,5])
plt.plot([15,15], [5,3])
plt.plot([15,13], [3,3])
plt.plot([13,15], [3,0])

#Letra E
plt.plot([17,17], [0,5])
plt.plot([17,19], [5,5])
plt.plot([17,19], [3,3])
plt.plot([17,19], [0,0])

#Letra S
# -------- Parte superior --------
t1 = np.linspace(np.pi/4, 3*np.pi/2, 100)  #Empieza en 45° termina en 270°
x1 = 1.25*np.cos(t1) + 22  # Se desplaza 22 en x y amplitud de 1.25
y1 = 1.25*np.sin(t1) + 3.75  # Se desplza 3.75 en y y amplitud de 1.25

# -------- Parte inferior --------
t2 = np.linspace(-3*np.pi/4, np.pi/2, 100) #Empieza en - 135° termina en 90°
x2 = 1.25*np.cos(t2) + 22 # Se desplaza 22 en x y amplitud de 1.25
y2 = 1.25*np.sin(t2) + 1.25 # Se desplza 1.25 en y y amplitud de 1.25

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.title("ANDRES")
plt.axis('equal')
plt.grid()


#Graficar todas las figuras

plt.show()