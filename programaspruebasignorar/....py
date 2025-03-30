def numprimo(n):
    if n < 2:
       return False 
    for i in range(2, int(n**0.5+1)):
       if n % i == 0:
           return False
    return True

numero = int(input("Ingresa un número: "))
print(f"El número {numero} {'es primo' 
if numprimo(numero) 
else 'no es primo'}")