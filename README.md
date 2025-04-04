Control de Inventario para negocios pequeños

Es un programa que maneja un inventario de productos, donde puedes agregar productos, mostrar el inventario, actualizar el stock y eliminar productos, todo esto guardando los datos en un archivo de texto llamado inventario.txt. El programa también carga los datos del archivo cada vez que se ejecuta, lo que permite mantener el inventario actualizado entre ejecuciones del programa.
1. Importación de Librerías
El código comienza importando la librería os. Esta librería se usa para interactuar con el sistema operativo, y en este caso, su función principal es verificar si el archivo de inventario existe antes de intentar leerlo.
2. Definir el archivo de inventario
Se define una variable archivo, que almacena el nombre del archivo de inventario. En este caso, el archivo se llama inventario.txt. Si el archivo no existe, el programa lo creará automáticamente cuando se guarde la información del inventario.
3. Función para Cargar el Inventario
La función cargar_inventario() se encarga de leer el archivo inventario.txt y cargar la información en un diccionario. Si el archivo existe, el programa lo abre en modo de lectura y lee cada línea. Cada línea contiene un producto, con su nombre, precio y cantidad. Estos datos se separan por comas, y luego se almacenan en un diccionario, donde la clave es el nombre del producto y el valor es otro diccionario con el precio y la cantidad.
4. Función para Guardar el Inventario
La función guardar_inventario(productos) guarda los datos del inventario en el archivo inventario.txt. Se abre el archivo en modo de escritura, lo que borra cualquier dato previo en el archivo, y luego se escriben los productos actuales. Cada producto se guarda en una línea, con el nombre, el precio y la cantidad, separados por comas.
5. Agregar Producto
La función agregar_producto(productos, nombre, precio, cantidad) permite agregar un nuevo producto al inventario o actualizar la cantidad de un producto existente. Si el producto ya está en el inventario, simplemente se aumenta la cantidad. Si el producto no está, se agrega con el precio y la cantidad proporcionados. Luego, se llama a la función guardar_inventario() para actualizar el archivo con los nuevos datos.
6. Mostrar Inventario
La función mostrar_inventario(productos) muestra todos los productos en el inventario, junto con su precio y cantidad. Si el inventario está vacío, se muestra un mensaje indicando que no hay productos.
7. Actualizar Stock
La función actualizar_stock(productos, nombre, nueva_cantidad) permite actualizar la cantidad de un producto en el inventario. Si el producto existe, se cambia su cantidad a la nueva cantidad proporcionada. Si el producto no se encuentra en el inventario, se muestra un mensaje de error. Después de actualizar, se guarda el inventario actualizado en el archivo.
8. Eliminar Producto
La función eliminar_producto(productos, nombre) permite eliminar un producto del inventario. Si el producto existe, se elimina del diccionario. Si el producto no se encuentra, se muestra un mensaje de error. Luego, el inventario actualizado se guarda en el archivo.
9. Menú Interactivo
El programa presenta un menú interactivo donde el usuario puede elegir entre varias opciones:
Agregar un producto: El usuario ingresa el nombre, precio y cantidad del producto que desea agregar.


Mostrar el inventario: Muestra todos los productos en el inventario actual.


Actualizar stock: Permite modificar la cantidad de un producto existente.


Eliminar un producto: Elimina un producto específico del inventario.


Salir: Finaliza la ejecución del programa.


10. Ejecución del Programa
Cuando el programa se ejecuta, primero carga el inventario desde el archivo, y luego muestra el menú para que el usuario pueda interactuar. Dependiendo de la opción que elija el usuario, el programa realizará una de las acciones descritas anteriormente y actualizará el archivo de inventario después de cada cambio.
