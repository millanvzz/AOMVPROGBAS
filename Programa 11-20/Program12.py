#Numero mayor de tres
def mayor(num1,num2,num3): #Funcion principal
    return max(num1,num2,num3)

num1=float(input("Introduzca el primer numero")) #Introduccion de variables
num2=float(input("Introduzca el segundo numero"))
num3=float(input("Introduzca el tercer numero")) 

print(f"El numero mayor de los tres es:", mayor(num1,num2,num3)) #Salida