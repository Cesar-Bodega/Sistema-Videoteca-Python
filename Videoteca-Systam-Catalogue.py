# Nombres del estudiante / Autor del codigo: Cesar Manuel Novoa Perilla
# Grupo: 213022_982 
# Tutor del curso UNAD: Nieder Duan Barbosa Castro
# Programa: Listado de Peliculas Videoteca Digital
# Descripcion: Programa que muestra un listado a base de categorias las cuales cumple respectivos requisitos de la  misma.


       #Titulo | Fecha | Calificacion
Peliculas =[

    ["Shin Godzilla", 2016, 7],
    ["Guerra de mundos", 2005, 7],
    ["Titanes del pacifico", 2013, 7],
    ["Tortugas Ninja", 2014, 5],
    ["La falla de san andreas", 2015, 5],
    ["Tiburon de 2 cabezas", 2015, 1],
    ["Pajaro loco", 2017, 3]
]

# Función que imprime los títulos de las películas populares incluyendo un contador.
def imprimir_titulos_populares(peliculas):
    contador = 0
    for pelicula in peliculas:
        contador += 1
        titulo = pelicula[0]   # columna 0: título
        año = pelicula[1]      # columna 1: año
        rate = pelicula[2]     # columna 2: calificación
        if año <= 2017 and rate >= 7:
            # Solo mostrar si ambas condiciones son verdaderas
            print(f"{contador}. {titulo}")
 # Función que imprime los títulos de las películas de nicho incluyendo un contador.

def imprimir_titulos_nicho(peliculas):
    contador = 0
    for pelicula in peliculas:
        contador += 1
        titulo = pelicula[0]
        año = pelicula[1]
        rate = pelicula[2]
        if año <= 2017 and rate < 7:
            print(f"{contador}. {titulo}")

# Dibuja en pantalla las opciones del menú principal.
def mostrar_menu():
    print("=== Menú de Videoteca ===")
    print("1. Mostrar Peliculas populares de los años")
    print("2. Mostrar Peliculas de nicho")
    print("0. Salir")

# Funcion de vista que manda a imprimir las peliculas populares.
def peliculas_populares():
    print("\nPeliculas Populares:")
    imprimir_titulos_populares(Peliculas)
    input("\nPresiona Enter para volver al menú principal...")
    
# Función de vista que manda a imprimir las peliculas de nicho.
def peliculas_nicho():    
    print("\nPeliculas de nicho:")
    imprimir_titulos_nicho(Peliculas)
    input("\nPresiona Enter para volver al menú principal...")
# Ambas funciones mandan a imprimir en su respectiva categoria y tienen la misma estructura de filtros pero con diferente cumplimiento.

# Esta funcion ejecuta otra funcion segun la opcion elegida.
def ejecutar_opcion(opcion):
    if opcion == "1":
        peliculas_populares()
    elif opcion == "2":
        peliculas_nicho()
    elif opcion == "0":
        print("Saliendo...")
    else:
        print("Opción no válida. Intenta otra vez.")

# Funcion que imprime el menu que se muestra a traves de un boleano y mantiene el programa activo hasta que se decida salir.
def main():
    menu_activo = True
    while menu_activo:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "0":
            ejecutar_opcion(opcion)
            menu_activo = False  # desactiva el menú para terminar
        else:
            ejecutar_opcion(opcion)
        print()  # línea en blanco entre vueltas del menú

if __name__ == "__main__":
    main()


