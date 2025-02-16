#Editar, crear uy leer el archivo de texto
path = "C:/Users/Alan Millan/Desktop/" #Ubicacion del archivo
name = "ARCHIVO"
ext = "aomv"

ARCHIVO = open(path+name+"1.txt","a", encoding="utf8") #Archivo a editar
print("Te amo amor mio. ", file=ARCHIVO)


ARCHIVO.close()#Cerrar el archivo
