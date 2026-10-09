#MINI PROYECTO DE RECURSIVIDAD
class ExploradorRecursivo:
    def __init__(self, sistema_archivos):
        self.sistema_archivos = sistema_archivos

    def imprimir_arbol(self, sistema=None, nivel=0):
        if sistema is None:
            sistema = self.sistema_archivos

        for nombre, contenido in sistema.items():
            # Caso recursivo: si es un diccionario (carpeta)
            if isinstance(contenido, dict):
                print("  " * nivel + f"- {nombre}/")
                self.imprimir_arbol(contenido, nivel + 1)
            # Caso base: si es un archivo
            else:
                print("  " * nivel + f"  * {nombre} ({contenido})")

    def buscar_archivo(self, nombre_objetivo, sistema=None, ruta_actual=""):
        if sistema is None:
            sistema = self.sistema_archivos

        for clave, valor in sistema.items():
            # Caso recursivo: explorar subcarpeta
            if isinstance(valor, dict):
                nueva_ruta = f"{ruta_actual}/{clave}" if ruta_actual else clave
                resultado = self.buscar_archivo(nombre_objetivo, valor, nueva_ruta)
                if resultado:
                    return resultado
            # Caso base: archivo encontrado
            elif clave.lower() == nombre_objetivo.lower():
                return f"{ruta_actual}/{clave}" if ruta_actual else clave

        # Caso base: no se encontro el archivo
        return None

    def contar_archivos(self, sistema=None):
        if sistema is None:
            sistema = self.sistema_archivos

        total = 0
        for clave, valor in sistema.items():
            # Caso recursivo: contar archivos dentro de la carpeta
            if isinstance(valor, dict):
                total += self.contar_archivos(valor)
            # Caso base: sumar 1 por cada archivo
            else:
                total += 1

        return total

    def calcular_peso_total(self, sistema=None):
        if sistema is None:
            sistema = self.sistema_archivos

        total_kb = 0.0
        for clave, valor in sistema.items():
            # Caso recursivo
            if isinstance(valor, dict):
                total_kb += self.calcular_peso_total(valor)
            # Caso base: convertir tamanos a KB
            else:
                texto = str(valor).lower().strip()
                if "mb" in texto:
                    total_kb += float(texto.replace("mb", "")) * 1024
                elif "kb" in texto:
                    total_kb += float(texto.replace("kb", ""))

        return total_kb


# Menu interactivo en consola
if __name__ == "__main__":
    sistema_archivos = {
        "Documentos": {
            "Ejercicios de recursividad": "10kb",
            "fotos": {
                "vacaciones.png": "2mb",
                "perro.jpg": "1mb",  
                "Mini proyecto de recursividad.py": "5kb"
            }
        },
        "sistema.dll": "500kb"
    }
    explorador = ExploradorRecursivo(sistema_archivos)

    opcion = ""
    while opcion != "5":
        print("\n=== MENU EXPLORADOR RECURSIVO ===")
        print("1. Mostrar arbol de archivos")
        print("2. Buscar archivo por nombre")
        print("3. Contar total de archivos")
        print("4. Calcular peso total")
        print("5. Salir")
        
        opcion = input("Ingrese una opcion (1-5): ").strip()

        if opcion == "1":
            print("\n--- Estructura de archivos ---")
            explorador.imprimir_arbol()

        elif opcion == "2":
            nombre_archivo = input("\nIngrese el nombre del archivo a buscar  ").strip()
            busqueda = explorador.buscar_archivo(nombre_archivo)
            if busqueda:
                print(f"-> Archivo encontrado en: /{busqueda}")
            else:
                print("-> Archivo no encontrado.")

        elif opcion == "3":
            total = explorador.contar_archivos()
            print(f"\n-> Total de archivos en el sistema: {total}")

        elif opcion == "4":
            peso = explorador.calcular_peso_total()
            print(f"\n-> Peso total del sistema: {peso:.2f} KB ({peso/1024:.2f} MB)")

        elif opcion == "5":
            print("\nSaliendo del programa...")

        else:
            print("\nOpcion no valida, intente de nuevo.")