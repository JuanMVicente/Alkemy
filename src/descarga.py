import categorias
import requests
import nombre_archivo

# Descarga los archivos de la web, genera carpetas y graba los archivos correspondientes
def descarga():
    categorys = categorias.categorys
    for category in categorys:
        name_file = nombre_archivo.nombre(category)
        #bajo el archivo
        r = requests.get(categorys[category]) # URL de la categoría
        f = open(name_file, "wb")
        f.write(r.content)
        f.close()
    return
