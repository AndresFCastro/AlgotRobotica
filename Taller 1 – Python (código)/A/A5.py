import math


def rotacion_x(angulo):
    theta = math.radians(angulo)
    return [
        [1, 0, 0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta), math.cos(theta)]
    ]


def rotacion_y(angulo):
    theta = math.radians(angulo)
    return [
        [math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [-math.sin(theta), 0, math.cos(theta)]
    ]


def rotacion_z(angulo):
    theta = math.radians(angulo)
    return [
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1]
    ]


angulo = 30  # grados

# Calcular matrices
Rx = rotacion_x(angulo)
Ry = rotacion_y(angulo)
Rz = rotacion_z(angulo)

# Imprimir resultados
print("Matriz de rotación en X:")
for fila in Rx:
    print([round(valor, 4) for valor in fila])

print("\nMatriz de rotación en Y:")
for fila in Ry:
    print([round(valor, 4) for valor in fila])

print("\nMatriz de rotación en Z:")
for fila in Rz:
    print([round(valor, 4) for valor in fila])
