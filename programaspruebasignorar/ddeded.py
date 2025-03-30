def es_palindromo(palabra):
    palabra = palabra
    return palabra == palabra[::-1]

palabra = input("Ingresa una palabra: ")
if es_palindromo(palabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")