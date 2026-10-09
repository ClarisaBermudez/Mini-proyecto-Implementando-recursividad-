# Ejercicios de recursividad 3
def imprimir_patron(n: int, actual: int = 1):
    """Imprime un patrón creciente de asteriscos hasta n filas de forma recursiva.

    Análisis Big-O:
    - Complejidad Temporal: O(N) -> Realiza N llamadas recursivas para N filas.
    - Complejidad Espacial: O(N) -> Profundidad máxima de N en la pila de llamadas.
    """
    # CASO BASE: Se alcanza el límite de filas solicitado
    if actual > n:
        return

    # Imprimir la fila actual de asteriscos
    print("*" * actual)

    # CASO RECURSIVO: Avanzar a la siguiente fila
    imprimir_patron(n, actual + 1)


# ENTRADA INTERACTIVA DE DATOS
print("--- PATRÓN DE ASTERISCOS ---")
filas = int(input("Ingresa el número de filas (n): "))

print("\nResultado:")
imprimir_patron(filas)
