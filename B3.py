import math

print("=== CALCULO DE VOLUMENES ===")
print("1. Prisma")
print("2. Piramide")
print("3. Cono truncado")
print("4. Cilindro")

op = int(input("Seleccione una opcion: "))

if op == 1:
    Ab = float(input("Ingrese el area de la base: "))
    h = float(input("Ingrese la altura: "))
    V = Ab * h
    print(f"Volumen del prisma: {V:.2f}")

elif op == 2:
    Ab = float(input("Ingrese el area de la base: "))
    h = float(input("Ingrese la altura: "))
    V = (Ab * h) / 3
    print(f"Volumen de la piramide: {V:.2f}")

elif op == 3:
    R = float(input("Ingrese el radio mayor: "))
    r = float(input("Ingrese el radio menor: "))
    h = float(input("Ingrese la altura: "))
    V = (1/3) * math.pi * h * (R**2 + R*r + r**2)
    print(f"Volumen del cono truncado: {V:.2f}")

elif op == 4:
    r = float(input("Ingrese el radio: "))
    h = float(input("Ingrese la altura: "))
    V = math.pi * r**2 * h
    print(f"Volumen del cilindro: {V:.2f}")

else:
    print("Opcion no valida.")
