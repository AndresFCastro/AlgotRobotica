print("=== TIPOS DE ROBOTS ===")
print("1. Robot Cilindrico")
print("2. Robot Cartesiano")
print("3. Robot Esferico")

op = int(input("Seleccione una opcion: "))

if op == 1:
    print("Robot Cilindrico")
    print("Posee 3 articulaciones: 1 rotacional y 2 prismaticas.")

elif op == 2:
    print("Robot Cartesiano")
    print("Posee 3 articulaciones prismaticas (movimiento en X, Y, Z).")

elif op == 3:
    print("Robot Esferico")
    print("Posee 3 articulaciones: 2 rotacionales y 1 prismatica.")

else:
    print("Opcion no valida.")
