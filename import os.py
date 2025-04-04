import os
archivo = "inventario.txt"

def cargar_inventario():
    productos = {}
    # Intentamos abrir el archivo de inventario
    file = open(archivo, 'r')  # Abrimos el archivo en modo lectura
    if file:  # Verificamos si el archivo existe
        for linea in file:
            nombre, precio, cantidad = linea.strip().split(",")  # Extraemos los datos
            productos[nombre] = {"precio": float(precio), "cantidad": int(cantidad)}  # Añadimos el producto al diccionario
        file.close()  # Cerramos el archivo al terminar de leerlo
    return productos

def guardar_inventario(productos):
    # Guardamos los productos en el archivo de inventario
    file = open(archivo, 'w')  # Abrimos el archivo en modo escritura
    for nombre, datos in productos.items():
        file.write(f"{nombre},{datos['precio']},{datos['cantidad']}\n")  # Escribimos cada producto
    file.close()  # Cerramos el archivo al terminar de escribir

def agregar_producto(productos, nombre, precio, cantidad):
    if nombre in productos:
        productos[nombre]["cantidad"] += cantidad  # Si el producto existe, agregamos más unidades
        print(f"Se agregaron {cantidad} unidades a '{nombre}'. Nuevo stock: {productos[nombre]['cantidad']}")
    else:
        productos[nombre] = {"precio": precio, "cantidad": cantidad}  # Si no existe, lo agregamos
        print(f"Producto '{nombre}' agregado con éxito.")
    guardar_inventario(productos)  # Guardamos los cambios en el archivo

def mostrar_inventario(productos):
    if not productos:
        print("El inventario está vacío.")
    else:
        print("\nInventario actual:")
        for nombre, datos in productos.items():
            print(f"- {nombre}: ${datos['precio']} - Stock: {datos['cantidad']}")

def actualizar_stock(productos, nombre, nueva_cantidad):
    if nombre in productos:
        productos[nombre]["cantidad"] = nueva_cantidad  # Actualizamos la cantidad del producto
        print(f"Stock de '{nombre}' actualizado a {nueva_cantidad}.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")
    guardar_inventario(productos)  # Guardamos los cambios en el archivo

def eliminar_producto(productos, nombre):
    if nombre in productos:
        del productos[nombre]  # Eliminamos el producto del inventario
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"Producto '{nombre}' no encontrado.")
    guardar_inventario(productos)  # Guardamos los cambios en el archivo

def mostrar_menu():
    print("\n----- MENÚ -----")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Actualizar stock")
    print("4. Eliminar producto")
    print("5. Salir")
    return input("Elige una opción: ")

def ejecutar_menu():
    productos = {}  # Inicializamos el diccionario de productos vacío
    try:
        productos = cargar_inventario()  # Intentamos cargar el inventario desde el archivo
    except:
        print("No se encontró el archivo de inventario. Se creará uno nuevo.")  # Si el archivo no existe, informamos al usuario
    
    while True:
        opcion = mostrar_menu()  # Mostramos el menú
        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            agregar_producto(productos, nombre, precio, cantidad)
        elif opcion == "2":
            mostrar_inventario(productos)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            actualizar_stock(productos, nombre, nueva_cantidad)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(productos, nombre)
        elif opcion == "5":
            print("Saliendo... ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción correcta.")

if __name__ == "__main__":
    ejecutar_menu()  # Ejecutamos el menú cuando se inicia el programa2