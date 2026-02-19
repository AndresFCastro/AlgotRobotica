import math


presion_bar = 6  # bar
diametro_piston_mm = 80  # mm
diametro_vastago_mm = 25  # mm


presion = presion_bar * 100000  # Pa
D = diametro_piston_mm / 1000  # m
d = diametro_vastago_mm / 1000  # m


def fuerza_avance(P, D):
    area = math.pi * (D**2) / 4
    return P * area

def fuerza_retroceso(P, D, d):
    area = math.pi * (D**2 - d**2) / 4
    return P * area

