# Ejercicios de recursividad 1
def multiplicacion_rusa(a: int, b: int) -> int:
    """Multiplica dos números enteros mediante el método ruso de forma recursiva.

    Análisis Big-O:
    - Complejidad Temporal: O(log A) -> El valor de 'a' se reduce a la mitad en cada paso.
    - Complejidad Espacial: O(log A) -> Profundidad de la pila de llamadas proporcional a log2(A).
    """
    # CASO BASE: Cuando el multiplicador llega a 0
    if a == 0:
        return 0

    # CASO RECURSIVO: Si 'a' es impar, sumamos 'b'; si es par, sumamos 0.
    # 'a' se divide entre 2 (división entera //) y 'b' se duplica (b * 2).
    actual = b if a % 2 != 0 else 0
    return actual + multiplicacion_rusa(a // 2, b * 2)


# ENTRADA INTERACTIVA DE DATOS
print("--- MULTIPLICACIÓN RUSA ---")
num1 = int(input("Ingresa el primer número (A): "))
num2 = int(input("Ingresa el segundo número (B): "))

# CÁLCULO Y RESULTADO
resultado = multiplicacion_rusa(num1, num2)
print(f"El resultado de multiplicar {num1} x {num2} es: {resultado}") 
