path = "C:/Users/Alan Millan/Desktop/"
name = "ARCHIVO"
ext = "aomv"

ARCHIVO = open(path+name+"1.txt","a", encoding="utf8")
print("Te amo amor mio. ", file=ARCHIVO)


ARCHIVO.close()
