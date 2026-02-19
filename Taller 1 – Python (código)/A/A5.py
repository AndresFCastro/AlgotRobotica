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


