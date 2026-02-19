vector1 = [2, 4, 6]
vector2 = [1, 3, 5]

def suma_vectores(v1, v2):
    return [a + b for a, b in zip(v1, v2)]

def resta_vectores(v1, v2):
    return [a - b for a, b in zip(v1, v2)]

def multiplicacion_elemento(v1, v2):
    return [a * b for a, b in zip(v1, v2)]

def division_elemento(v1, v2):
    return [a / b if b != 0 else None for a, b in zip(v1, v2)]

def producto_punto(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

def producto_cruz(v1, v2):
    return [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]


# Mostrar resultados
print("Suma:", suma_vectores(vector1, vector2))
print("Resta:", resta_vectores(vector1, vector2))
print("Multiplicación:", multiplicacion_elemento(vector1, vector2))
print("División:", division_elemento(vector1, vector2))
print("Producto Punto:", producto_punto(vector1, vector2))
print("Producto Cruz:", producto_cruz(vector1, vector2))