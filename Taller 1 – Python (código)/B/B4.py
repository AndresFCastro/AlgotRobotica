print("TIPOS DE ROBOTS")
print("1. Robot Cilindrico")
print("2. Robot Cartesiano")
print("3. Robot Esferico")

opcion = int(input("Seleccione una opcion: "))

if opcion == 1:
    print("Robot Cilindrico")
    print("Posee 3 articulaciones: 1 articulacion de revolucion (rotacional) y 2 prismaticas (lineales).")

elif opcion == 2:
    print("Robot Cartesiano")
    print("Posee 3 articulaciones prismaticas (movimientos lineales en X, Y, Z).")

elif opcion == 3:
    print("Robot Esferico")
    print("Posee 3 articulaciones: 2 articulaciones rotativas (giro y elevacion) y 1 prismatica (extension).")

else:
    print("Opcion no valida.")
