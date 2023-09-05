def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

def ordenar_fila(matriz, fila):
    # Verificar si la fila es válida
    if fila < 0 or fila >= len(matriz):
        print("Fila no válida")
        return

    # Utilizar el algoritmo de ordenación (Bubble Sort)
    n = len(matriz[0])
    for i in range(n - 1):
        for j in range(n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Definir una matriz de ejemplo (3x3)
matriz = [
    [3, 1, 4],
    [1, 5, 9],
    [2, 6, 5]
]

# Mostrar la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Ordenar la fila 1 (índice 0)
ordenar_fila(matriz, 0)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
imprimir_matriz(matriz)
