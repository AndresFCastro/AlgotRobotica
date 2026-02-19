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

# ==========================
# CÁLCULO
# ==========================

F_avance = fuerza_avance(presion, D)
F_retroceso = fuerza_retroceso(presion, D, d)

# ==========================
# IMPRESIÓN
# ==========================

print(f"Presión: {presion_bar} bar")
print(f"Diámetro pistón: {diametro_piston_mm} mm")
print(f"Diámetro vástago: {diametro_vastago_mm} mm\n")

print(f"Fuerza de avance: {F_avance:.2f} N")
print(f"Fuerza de retroceso: {F_retroceso:.2f} N")