#Funciones_LorenaFigueroa_FPY1101_009V

import os

libros = []
sku = []
libros_prestados = []

def registro():
    try:
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el nombre del autor del libro: ")
        ano_publicacion = int(input("Ingrese el año de publicación del libro: "))
        sku = input("Ingrese el SKU: ")
        

        if titulo == "" or autor == "" or ano_publicacion <=0:
            print("Faltaron datos por ingresar")

        libro ={ 
            'titulo':titulo.upper(),
            'autor':autor.upper(),
            'ano_publicacion':ano_publicacion,
            'sku':sku,
            }
        libros.append(libro)
        print("Se ha realizado el registro con éxito")
    except ValueError:
        print("Dato Erróneo, vuelva a intentar")

def prestamo():
    
    nombre_usuario = input("Ingrese el nombre del usuario: ")
    sku_libro = input("Ingrese el SKU del libro: ")

    for sku in libros:
        if sku['sku'] == sku_libro:
            print("Libro existente")

            fecha_prestamo = input("Ingrese la fecha de préstamo: ")
            titulo = sku['titulo']

            libro_p = {
                'usuario': nombre_usuario.upper(),
                'titulo': titulo,
                'fecha_p' : fecha_prestamo,
                'sku': sku_libro,
            }
            libros_prestados.append(libro_p)
            print("Libro prestado con éxito") 
            rep=False
        else:
            print("El Libro no existe, vuelva a intentar")

def listar():
    print("TÍTULO\t\tAUTOR\tAÑO PUBLICACION\tSKU")
    for libro in libros:
        print(f"{libro['titulo']}\t{libro['autor']}\t{libro['ano_publicacion']}\t\t\t{libro['sku']}")

def imprimir():
    with open('detalle_prestamos.txt', 'w') as archivo:
        archivo.write("USUARIO\t\tAUTOR\tAÑO PUBLICACION\tSKU\n")
        for libro in libros_prestados:
            archivo.write(f"{libro['usuario']}\t{libro['titulo']}\t{libro['fecha_p']}\n")
    print("Planilla Generada con éxito")

def menu ():
    while True:
        try:
            print(" * * * M E N Ú * * * ")
            print("1. Registrar libro")
            print("2. Prestar libro")
            print("3. Listar todos los libros")
            print("4. Imprimir reporte de préstamos")
            print("5. Salir del Programa")

            op=int(input("Selecciones una opción del menú : "))
        except ValueError:
            print("Dato Erróneo, vuelva a intentar")
            continue
            
        if op == 1:
            registro()
        elif op == 2 :
            prestamo()
        elif op == 3 :
            listar()
        elif op ==4:
            imprimir()
        elif op == 5:
            print("Programa Finalizado\nDesarrollado por Lorena Figueroa\nRUT: 17.674.651-3")
            break