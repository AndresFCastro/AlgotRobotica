print("CALCULO DE POTENCIA ELECTRICA")

voltaje = float(input("Ingrese el valor del voltaje (V): "))
corriente = float(input("Ingrese el valor de la corriente (A): "))

potencia = voltaje * corriente

print(f"La potencia es: {potencia:.2f} Watts (W)")
