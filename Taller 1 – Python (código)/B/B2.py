import random

print("GENERADOR DE NUMEROS ALEATORIOS")

numeros = int(input("Cuantos numeros desea generar?: "))
rangominimo = float(input("Ingrese el valor minimo del rango: "))
rangomaximo = float(input("Ingrese el valor maximo del rango: "))

print("Numeros generados:")

for i in range(numeros):
    numero = random.uniform(rangominimo, rangomaximo)
    print(f"{numero:.0f}")
