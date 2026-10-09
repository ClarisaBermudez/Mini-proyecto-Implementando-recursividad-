# Ejercicios de recursividad 5
def aplanar_lista(lista: list) -> list:
    """Recibe una lista con elementos o sublistas anidadas y devuelve una lista plana.

    Análisis Big-O:
    - Complejidad Temporal: O(N) -> Donde N es el total de elementos individuales dentro de la estructura.
    - Complejidad Espacial: O(D) -> D es el nivel máximo de anidamiento de las sublistas.
    """
    resultado = []
    
    for elemento in lista:
        if isinstance(elemento, list):
            # CASO RECURSIVO: Si es una sublista, se aplana recursivamente y se extiende
            resultado.extend(aplanar_lista(elemento))
        else:
            # CASO BASE IMPLÍCITO: Si es un valor individual, se agrega directamente
            resultado.append(elemento)
            
    return resultado


# ENTRADA INTERACTIVA DE DATOS
print("--- APLANAR LISTA ANIDADA (FLATTEN LIST) ---")
entrada_str = input("Ingresa una lista anidada  ")

# Convertir el texto ingresado por el usuario en una lista real de Python
import ast
lista_usuario = ast.literal_eval(entrada_str)

# CÁLCULO Y RESULTADO
lista_plana = aplanar_lista(lista_usuario)
print(f"\nLista aplanada: {lista_plana}")