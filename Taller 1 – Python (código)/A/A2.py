
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]


def suma_matrices(m1, m2):
    return [
        [m1[i][j] + m2[i][j] for j in range(len(m1[0]))]
        for i in range(len(m1))
    ]


def resta_matrices(m1, m2):
    return [
        [m1[i][j] - m2[i][j] for j in range(len(m1[0]))]
        for i in range(len(m1))
    ]


def multiplicacion_matrices(m1, m2):
    resultado = [[0, 0], [0, 0]]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                resultado[i][j] += m1[i][k] * m2[k][j]
    return resultado


def division_matrices(m1, m2):
    return [
        [
            m1[i][j] / m2[i][j] if m2[i][j] != 0 else None
            for j in range(len(m1[0]))
        ]
        for i in range(len(m1))
    ]


# Mostrar resultados
print("Suma:", suma_matrices(A, B))
print("Resta:", resta_matrices(A, B))
print("Multiplicación:", multiplicacion_matrices(A, B))
print("División:", division_matrices(A, B))
