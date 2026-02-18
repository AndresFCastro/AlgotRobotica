import random

print("=== GENERADOR DE NUMEROS ALEATORIOS ===")

n = int(input("¿Cuantos numeros desea generar?: "))
min_val = float(input("Ingrese el valor minimo del rango: "))
max_val = float(input("Ingrese el valor maximo del rango: "))

print("Numeros generados:")

for i in range(n):
    numero = random.uniform(min_val, max_val)
    print(f"{numero:.2f}")
