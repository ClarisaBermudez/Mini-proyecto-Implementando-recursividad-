# Ejercicios de recursividad 4
def contar_caminos(n: int, m: int) -> int:
    """Calcula el número de caminos posibles en una matriz NxM desde (0,0) hasta (N-1, M-1).

    Análisis Big-O:
    - Complejidad Temporal: O(2^(N+M)) -> Explora dos ramas recursivas (abajo y derecha) en cada casilla.
    - Complejidad Espacial: O(N + M) -> La profundidad máxima de la pila es la distancia del camino.
    """
    # CASO BASE: Si el tablero es de 1xM o Nx1, solo hay 1 camino único posible (en línea recta)
    if n == 1 or m == 1:
        return 1

    # CASO RECURSIVO: Caminos moviéndose hacia abajo (n-1) + caminos moviéndose a la derecha (m-1)
    return contar_caminos(n - 1, m) + contar_caminos(n, m - 1)


# ENTRADA INTERACTIVA DE DATOS
print("--- CAMINOS EN UN TABLERO ---")
filas = int(input("Ingresa el número de filas (N): "))
columnas = int(input("Ingresa el número de columnas (M): "))

# CÁLCULO Y RESULTADO
total_caminos = contar_caminos(filas, columnas)
print(f"\nEl número total de caminos en un tablero de {filas}x{columnas} es: {total_caminos}")