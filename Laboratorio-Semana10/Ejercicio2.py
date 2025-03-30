class Inventario:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self):
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        self.productos.append({
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "cantidad": cantidad
        })
        print(f"Producto '{nombre}' agregado al inventario.")
    
    def eliminar_producto(self):
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        self.productos = [p for p in self.productos if p["nombre"] != nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    
    def buscar_producto(self):
        nombre = input("Ingrese el nombre del producto a buscar: ")
        for producto in self.productos:
            if producto["nombre"] == nombre:
                print("Información del producto:")
                for key, value in producto.items():
                    print(f"{key.capitalize()}: {value}")
                return
        print(f"Producto '{nombre}' no encontrado.")
    
    def mostrar_productos_ordenados(self):
        productos_ordenados = sorted(self.productos, key=lambda x: x["precio"])
        print("\nInventario ordenado por precio:")
        for producto in productos_ordenados:
            print(f"{producto['nombre']} - Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

# Menú de opciones
inventario = Inventario()
while True:
    print("\nMenú de Inventario:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    print("4. Mostrar productos ordenados por precio")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        inventario.agregar_producto()
    elif opcion == "2":
        inventario.eliminar_producto()
    elif opcion == "3":
        inventario.buscar_producto()
    elif opcion == "4":
        inventario.mostrar_productos_ordenados()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
