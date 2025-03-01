#Implementar una agenda de contactos

bandera=True
contador=1
listacontactos= list()

while bandera:
    op=input(f"Cantidad de contactos: {contador-1} n Desea agregar un contacto? (s/n) ")
    if op.lower()=='s' or op.lower()=='S':
        contacto= dict()
        contacto["identificador"]= input(f"Ingrese el identificador del {contador}: ")
        contacto["Numero"]=  input(f"ingrese el numero de contacto {contador}: ")
        contador +=1
        listacontactos.append(contacto)
    else:
        break

print(listacontactos)