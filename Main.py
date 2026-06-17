import csv
import os

#Archivo donde almacenamos los datos de los países
ARCHIVO_CSV = "paises.csv"

#Funciones de lectura y escritura
def cargar_paises():
    paises = []

    if not os.path.exists(ARCHIVO_CSV):
        return paises

    try:
        with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                paises.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                })

    except Exception as e:
        print("Error al leer el CSV:", e)

    return paises


#Sobrescribe la lista de países en el archivo CSV
def guardar_paises(paises):
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:

        campos = [
            "nombre",
            "poblacion",
            "superficie",
            "continente"
        ]

        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)


#Funciones de visualización
def mostrar_paises(paises):
    if len(paises) == 0:
        print("\nNo hay países para mostrar.")
        return

    print("\n" + "=" * 90)

    print(
        f"{'NOMBRE':20}"
        f"{'POBLACION':15}"
        f"{'SUPERFICIE':15}"
        f"{'CONTINENTE':15}"
    )

    print("=" * 90)

    for pais in paises:

        print(
            f"{pais['nombre'].title():20}"
            f"{pais['poblacion']:<15}"
            f"{pais['superficie']:<15}"
            f"{pais['continente'].title():<15}"
        )

#Funciones de entrada / validaciones
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))

            if valor <= 0:
                print("Ingrese un número entero mayor a 0.")
                continue

            return valor

        except ValueError:
            print("Debe ingresar un número válido.")

def pedir_entero_no_negativo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))

            if valor < 0:
                print("Ingrese un número positivo.")
                continue

            return valor

        except ValueError:
            print("Debe ingresar un número válido.")

#Funciones para agregar y actualizar
def agregar_pais(paises):
    print("\n=== AGREGAR PAIS ===")

    nombre = input("Nombre: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    for pais in paises:

        if pais["nombre"].title() == nombre.title():
            print(f"El país {pais} ya existe, ingrese un país válido.")
            return

    poblacion = pedir_entero("Población: ")
    superficie = pedir_entero("Superficie km²: ")

    continente = input("Continente: ").strip()

    if continente == "":
        print("El continente no puede estar vacío.")
        return
    
    if not all(c.isalpha() or c.isspace() for c in continente):
        print("El continente solo puede contener letras.")
        return

    nuevo_pais = {
        "nombre": nombre.title(),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente.title()
    }

    paises.append(nuevo_pais)

    guardar_paises(paises)

    print("País agregado correctamente.")


def actualizar_pais(paises):
    print("\n=== ACTUALIZAR PAIS ===")

    nombre = input("Ingrese el nombre del país: ")

    for pais in paises:

        if pais["nombre"].title() == nombre.title():

            pais["poblacion"] = pedir_entero("Nueva población: ")
            pais["superficie"] = pedir_entero("Nueva superficie: ")

            nuevo_continente = input("Nuevo continente (Enter para mantener el actual): ").strip()
            if nuevo_continente != "":
                pais["continente"] = nuevo_continente.title()

            guardar_paises(paises)
            print("Los datos fueron actualizados correctamente.")
            return

    print("País no encontrado.")

#Funciones para buscar
def buscar_pais(paises):
    print("\n=== BUSCAR PAIS ===")

    pais = input("Ingrese el nombre del país que desea buscar (total o parcial): ").title()

    if pais == "":
        print("Debe ingresar al menos un carácter para buscar.")
        return    

    resultados = [p for p in paises if pais in p["nombre"].title()]

    if len(resultados) == 0:
        print("No se encontraron resultados.")
    else:
        mostrar_paises(resultados)


def filtrar_continente(paises):
    print("\n=== FILTRAR POR CONTINENTE ===")

    continente = input("Continente: ").strip().title()

    if continente == "":
        print("Debe ingresar un continente.")
        return
    
    resultado = [p for p in paises if p["continente"].title() == continente]

    if len(resultado) == 0:
        print(f"No se encontraron países para el continente {continente}.")
    else:
        mostrar_paises(resultado)


def filtrar_poblacion(paises):
    print("\n=== FILTRAR POR POBLACIÓN ===")

    minimo = pedir_entero_no_negativo("Población mínima: ")
    maximo = pedir_entero_no_negativo("Población máxima: ")

    if minimo > maximo:
        print("El mínimo no puede ser mayor al máximo.")
        return

    resultado = [p for p in paises if minimo <= p["poblacion"] <= maximo]

    if len(resultado) == 0:
        print("No se encontraron países en ese rango de población.")
    else:
        mostrar_paises(resultado)


def filtrar_superficie(paises):
    print("\n=== FILTRAR POR SUPERFICIE ===")

    minimo = pedir_entero_no_negativo("Superficie mínima: ")
    maximo = pedir_entero_no_negativo("Superficie máxima: ")

    resultado = []

    if minimo > maximo:
        print("El mínimo no puede ser mayor al máximo.")
        return

    resultado = [p for p in paises if minimo <= p["superficie"] <= maximo]

    if len(resultado) == 0:
        print("No se encontraron países en ese rango de superficie.")
    else:
        mostrar_paises(resultado)

#Submenu para filtros
def menu_filtros(paises):
    while True:

        print("\n=== FILTROS ===")
        print("1. Por continente")
        print("2. Por población")
        print("3. Por superficie")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":
            filtrar_continente(paises)
        elif opcion == "2":
            filtrar_poblacion(paises)
        elif opcion == "3":
            filtrar_superficie(paises)
        elif opcion == "0":
            break
        else:
            print("La opción ingresada no es válida.")


#Funciones para ordenar
def pedir_orden():
    while True:
        orden = input("A Ascendente / D Descendente: ").upper().strip()
        if orden in ("A", "D"):
            return orden
        print("Ingrese A para orden ascendente o D para orden descendente.")

def ordenar_nombre(paises):
    print("\n=== ORDENAR POR NOMBRE ===")
    orden = pedir_orden()
    ordenados = sorted(paises, key=lambda p: p["nombre"], reverse=(orden == "D"))

    mostrar_paises(ordenados)


def ordenar_poblacion(paises):
    print("\n=== ORDENAR POR POBLACIÓN ===")
    orden = pedir_orden()

    ordenados = sorted(paises, key=lambda p: p["poblacion"], reverse=(orden == "D"))
    mostrar_paises(ordenados)


def ordenar_superficie(paises):
    print("\n=== ORDENAR POR SUPERFICIE ===")
    orden = pedir_orden()

    ordenados = sorted(paises, key=lambda p: p["superficie"], reverse=(orden == "D"))
    mostrar_paises(ordenados)

#Submenu para opciones de orden
def menu_ordenar(paises):

    while True:

        print("\n=== ORDENAR ===")
        print("1. Nombre")
        print("2. Población")
        print("3. Superficie")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":
            ordenar_nombre(paises)
        elif opcion == "2":
            ordenar_poblacion(paises)
        elif opcion == "3":
            ordenar_superficie(paises)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

#Estadísticas
def estadisticas(paises):
    if len(paises) == 0:
        print("No hay datos para calcular estadísticas.")
        return

#País con mayor y menor población
    mayor = max(paises, key=lambda p: p["poblacion"])
    menor = min(paises, key=lambda p: p["poblacion"])

    promedio_poblacion = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_superficie = sum(p["superficie"] for p in paises) / len(paises)

    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n=== ESTADÍSTICAS ===")
    print(f"Mayor población : {mayor['nombre']} ({mayor['poblacion']:,})")
    print(f"Menor población : {menor['nombre']} ({menor['poblacion']:,})")
    print(f"Promedio población : {promedio_poblacion:,.2f}")
    print(f"Promedio superficie: {promedio_superficie:,.2f} km²")

    print("\nCantidad de países por continente:")
    for continente, cantidad in sorted(continentes.items()):
        print(f"  {continente}: {cantidad}")

#Menu principal
def menu():
    print("\n===== GESTION DE PAISES =====")
    print("1. Mostrar países")
    print("2. Agregar país")
    print("3. Actualizar país")
    print("4. Buscar país")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Estadísticas")
    print("0. Salir")


def main():
    paises = cargar_paises()

    while True:

        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_paises(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais(paises)
        elif opcion == "5":
            menu_filtros(paises)
        elif opcion == "6":
            menu_ordenar(paises)
        elif opcion == "7":
            estadisticas(paises)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("La opción ingresada no es válida. Ingrese un número del 1 al 7")

main()