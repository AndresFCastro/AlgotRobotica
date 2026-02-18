import math

print("CALCULO DE VOLUMENES")
print("1. Prisma")
print("2. Piramide")
print("3. Cono truncado")
print("4. Cilindro")

opcion = int(input("Seleccione una opcion: "))

if opcion == 1:
    Area_base = float(input("Ingrese el area de la base: "))
    Altura = float(input("Ingrese la altura: "))
    Volumen = Area_base * Altura
    print(f"Volumen del prisma: {Volumen:.2f}")

elif opcion == 2:
    Area_base = float(input("Ingrese el area de la base: "))
    Altura = float(input("Ingrese la altura: "))
    Volumen = (Area_base * Altura) / 3
    print(f"Volumen de la piramide: {Volumen:.2f}")

elif opcion == 3:
    Radio_grande = float(input("Ingrese el radio mayor: "))
    Radio_menor = float(input("Ingrese el radio menor: "))
    Altura = float(input("Ingrese la altura: "))
    Volumen = (1/3) * math.pi * Altura * (Radio_grande**2 + Radio_grande*Radio_menor + Radio_menor**2)
    print(f"Volumen del cono truncado: {Volumen:.2f}")

elif opcion == 4:
    Radio = float(input("Ingrese el radio: "))
    Altura = float(input("Ingrese la altura: "))
    Volumen = math.pi * Radio**2 * Altura
    print(f"Volumen del cilindro: {Volumen:.2f}")

else:
    print("Opcion no valida.")
