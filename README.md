# TPI_Programacion1

## Integrantes

| Nombre | Participación |
|--------|--------------|
| Agustina Balcarcel | Desarrollo, documentación |
| Araceli Ignes | Desarrollo, documentación |

# Gestión de Datos de Países

Aplicación de consola desarrollada en Python que permite gestionar información sobre países. El programa lee y escribe datos desde un archivo CSV, y ofrece funcionalidades de búsqueda, filtrado, ordenamiento y estadísticas.

Trabajo Práctico Integrador — Programación 1  
Tecnicatura Universitaria en Programación — UTN

## Instrucciones de uso

1. Clonar o descargar el repositorio.
2. Asegurarse de que el archivo `paises.csv` esté en la misma carpeta que `Main.py`.
3. Ejecutar el programa:
```
python Main.py
```

4. Navegar por el menú ingresando el número de la opción deseada.

---

## Funcionalidades

- **Mostrar países:** lista todos los países cargados en el sistema.
- **Agregar país:** solicita nombre, población, superficie y continente, y lo guarda en el CSV.
- **Actualizar país:** permite modificar la población, superficie y continente de un país existente.
- **Buscar país:** búsqueda por nombre con coincidencia parcial o exacta.
- **Filtrar países:** por continente, rango de población o rango de superficie.
- **Ordenar países:** por nombre, población o superficie, en orden ascendente o descendente.
- **Estadísticas:** muestra el país con mayor y menor población, promedios de población y superficie, y cantidad de países por continente.

---

## Ejemplos de entradas y salidas

### Agregar un país

```
=== AGREGAR PAIS ===
Nombre: chile
Población: 19000000
Superficie km²: 756102
Continente: america
País agregado correctamente.
```

### Buscar un país

```
=== BUSCAR PAIS ===
Ingrese el nombre del país que desea buscar (total o parcial): ar

==========================================================================================
NOMBRE              POBLACION      SUPERFICIE     CONTINENTE     
==========================================================================================
Argentina           45376763       2780400        America        
```

### Filtrar por continente

```
=== FILTRAR POR CONTINENTE ===
Continente: europa

==========================================================================================
NOMBRE              POBLACION      SUPERFICIE     CONTINENTE     
==========================================================================================
Alemania            83149300       357022         Europa         
Francia             68042591       551695         Europa         
```

### Estadísticas

```
=== ESTADÍSTICAS ===
Mayor población : China (1412600000)
Menor población : Uruguay (3554915)
Promedio población : 245.320.000,00
Promedio superficie: 1.234.567,00 km²

Cantidad de países por continente:
  America: 3
  Asia: 2
  Europa: 2
```

### Ordenar por población descendente

```
=== ORDENAR POR POBLACIÓN ===
A Ascendente / D Descendente: D

==========================================================================================
NOMBRE              POBLACION      SUPERFICIE     CONTINENTE     
==========================================================================================
China               1412600000     9596960        Asia           
India               1380004385     3287263        Asia           
Brasil              213993437      8515767        America        
```

---

## Estructura del proyecto

```
/
├── Main.py          # Código fuente principal
├── paises.csv       # Dataset base con países de ejemplo
└── README.md        # Este archivo
```


