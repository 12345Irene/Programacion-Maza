def buscar_valor(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == valor:
                return fila, columna
    return None

# Definir una matriz de ejemplo (3x3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Valor a buscar
valor_a_buscar = 5
# Realizar la busqueda
resultado = buscar_valor(matriz, valor_a_buscar)
if resultado:
    fila, columna = resultado
    print(f"El valor {valor_a_buscar} se concentrate en la position ({fila}, {columna}) de la matriz.")
else:
    print(f"El valor {valor_a_buscar} no se encontro en la matriz.")