#Calcular Area y volumen de figuras geometricas

import math

print("""Elija una opcion
1-.Area de un Cuadrado
2-.Area de un Rectangulo
3-.Area de un Circulo
4-.Volumen de un Cubo
5-.Volumen de un Cono
6-.Volumen de una Esfera

elija una opcion: """)

op=int(input(""))

if op==1:
    lado=int(input("Introduzca el lado del cuadrado: "))
    Area_cuadrado= lado**2
    print("El area del cuadrado es=", Area_cuadrado)
elif op==2:
    Base=int(input("Ingrese la base del rectangulo: "))
    Altura=int(input("Ingrese la altura del rectangulo: "))
    Area_Rectangulo= Base*Altura
    print("El area del rectangulo=", Area_Rectangulo)
elif op==3:
    Rad=int(input("Ingrese el radio del circulo: "))
    Area_Circulo= math.pi*(Rad**2)
    print("El area del circulo=",Area_Circulo)
elif op==4:
    lado_cub=int(input("Introduzca el lado del cubo: "))
    Vol_Cubo=lado_cub**3
    print("Volumen del cubo=", Vol_Cubo)
elif op==5:
    radio_con=int(input("Ingresa el radio del cono: "))
    altura_con=int(input("Ingrese la altura del cono: "))
    volumen_con= (math.pi*(radio_con*2)*altura_con/3)
    print("El volumen del cono es=", volumen_con)
elif op==6:
    rad_esf=int(input("Ingrese el radio de la esfera: "))
    vol_esf= ((4*math.pi*(rad_esf**3))/3)
    print("El volumen de la esfera es=", vol_esf)
elif (op<1) or (op>6):
    print("opcion invalida, intente de nuevo")