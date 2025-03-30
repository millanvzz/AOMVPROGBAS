# Definición de la lista que actuará como agenda de contactos
agenda = []

# Función para agregar un nuevo contacto a la agenda
def agregar_contacto():
    """
    Solicita al usuario los datos del contacto y lo agrega a la agenda.
    El contacto se almacena como una tupla (nombre, número, correo).
    """
    print("\n--- Agregar nuevo contacto ---")
    nombre = input("Nombre del contacto: ")
    telefono = input("Número de teléfono: ")
    correo = input("Correo electrónico: ")
    
    # Crear la tupla con los datos del contacto
    nuevo_contacto = (nombre, telefono, correo)
    
    # Añadimos el contacto a la agenda
    agenda.append(nuevo_contacto)
    print(f"Contacto '{nombre}' agregado con éxito")

# Función para buscar un contacto por nombre
def buscar_contacto():
    """
    Busca un contacto por nombre y muestra sus detalles si se encuentra.
    """
    print("\n--- Buscar contacto ---")
    nombre_buscar = input("Ingrese el nombre a buscar: ")
    
    encontrado = False
    for contacto in agenda:
        # El nombre es el primer elemento de la tupla (índice 0)
        if contacto[0].lower() == nombre_buscar.lower():
            print("\nContacto encontrado:")
            print(f"Nombre: {contacto[0]}")
            print(f"Teléfono: {contacto[1]}")
            print(f"Correo: {contacto[2]}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"No se encontró ningún contacto con el nombre '{nombre_buscar}'")

# Función para listar todos los contactos en orden alfabético
def listar_contactos():
    """
    Muestra todos los contactos de la agenda ordenados alfabéticamente por nombre.
    """
    print("\n--- Lista de contactos ---")
    
    if not agenda:
        print("La agenda está vacía.")
        return
    
    # Ordenar la agenda por nombre (primer elemento de cada tupla)
    agenda_ordenada = sorted(agenda, key=lambda x: x[0].lower())
    
    for i, contacto in enumerate(agenda_ordenada, 1):
        print(f"{i}. Nombre: {contacto[0]}, Teléfono: {contacto[1]}, Correo: {contacto[2]}")

# Menú principal del programa
def menu():
    """
    Muestra el menú principal y maneja las opciones del usuario.
    """
    while True:
        print("\n--- Gestión de Contactos ---")
        print("1. Agregar nuevo contacto")
        print("2. Buscar contacto")
        print("3. Listar todos los contactos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            listar_contactos()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1-4.")

# Ejecución del programa
if __name__ == "__main__":
    print("--Sistema de gestion de contactos--")
    menu()