# Ejercicios de recursividad 2
def contar_vocales(texto: str) -> int:
    """Calcula el número de vocales en un string de forma recursiva.

    Análisis Big-O:
    - Complejidad Temporal: O(N) -> Donde N es la longitud del string.
    - Complejidad Espacial: O(N) -> Pila proporcional a la longitud del texto.
    """
    # CASO BASE: String vacío
    if not texto:
        return 0

    # Determinar si el primer carácter es una vocal
    es_vocal = 1 if texto[0].lower() in "aeiouáéíóú" else 0

    # CASO RECURSIVO: Sumar la vocal actual y llamar con el resto de la cadena
    return es_vocal + contar_vocales(texto[1:])


# Pedir la palabra al usuario por la terminal
palabra = input("Escribe una palabra o frase: ")

# Mostrar cuántas vocales tiene
total = contar_vocales(palabra)
print(f"La palabra '{palabra}' tiene {total} vocales.")
