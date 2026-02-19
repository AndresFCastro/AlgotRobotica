import math


x = 3
y = 4
z = 5


def rectangular_a_cilindricas(x, y, z):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)  # en radianes
    return r, theta, z


def rectangular_a_esfericas(x, y, z):
    rho = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)  # en radianes
    phi = math.acos(z / rho)
    return rho, theta, phi

# Resultados
cilindricas = rectangular_a_cilindricas(x, y, z)
esfericas = rectangular_a_esfericas(x, y, z)

# Mostrar resultados (en grados para mejor interpretación)
print("Coordenadas Rectangulares:", (x, y, z))
print("\nCilíndricas (r, θ, z):")
print("r =", cilindricas[0])
print("θ =", math.degrees(cilindricas[1]), "grados")
print("z =", cilindricas[2])

print("\nEsféricas (ρ, θ, φ):")
print("ρ =", esfericas[0])
print("θ =", math.degrees(esfericas[1]), "grados")
print("φ =", math.degrees(esfericas[2]), "grados")
