#Simular una cuenta cuenta bancaria con depositos y retiros

saldo = 0

while True:
    print("Opciones:")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Ver saldo")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == 1:
        cantidad = float(input("¿Cuánto deseas depositar? $"))
        saldo += cantidad
        print("Saldo actual: $",saldo)
    elif opcion == 2:
        cantidad = float(input("¿Cuánto deseas retirar? $"))
        if cantidad <= saldo:
            saldo -= cantidad
            print("Saldo actual: $", saldo)
        else:
            print("Saldo insuficiente.")
    elif opcion == 3:
        print("Saldo actual: $",saldo)
    elif opcion == 4:
        break
    else:
        print("Opción no válida.")