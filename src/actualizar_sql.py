from datetime import date
from conexion_postgresql import crea_tabla_categoria, crea_tabla_cine, crea_tabla_fuente, crea_tabla_general, crea_tabla_provincia_categoria, inserta_tabla_categoria, inserta_tabla_cine, inserta_tabla_fuente, inserta_tabla_general, inserta_tabla_provincia_categoria

# funcion para actualizar toda la tabla consolidada con los datos generales del proyecto
def actualizar_tabla_general(general):
    # crea la tabla (si se encuentra creada la elimina y genera una nueva)
    crea_tabla_general()
    fecha = str(date.today())
    for row in general:
        if row[7] == "": row[7]= None
        if row[8] == "": row[8]= None
        if row[9] == "": row[9]= None
        if row[10] == "": row[10]= None
        if row[11] == "": row[11]= None
        localidad = str(row[5]).replace("'","_")
        nombre = str(row[6]).replace("'","_")
        direccion = str(row[7]).replace("'","_")
        datos = [row[0],row[1],row[2],row[3],row[4],localidad,nombre,direccion,row[8],row[9],row[10],row[11],fecha]
        inserta_tabla_general(datos)


# funcion para actualizar toda la tabla consolidada con los datos de catregoría del proyecto
def actualiza_tabla_categoria(categoria):
    # crea la tabla (si se encuentra creada la elimina y genera una nueva)
    crea_tabla_categoria()
    fecha = str(date.today())
    for key in categoria:
        datos = [key, categoria[key],fecha]
        inserta_tabla_categoria(datos)


# funcion para actualizar toda la tabla consolidada con los datos de fuente del proyecto
def actualiza_tabla_fuente(fuente):
    # crea la tabla (si se encuentra creada la elimina y genera una nueva)
    crea_tabla_fuente()
    fecha = str(date.today())
    for key in fuente:
        datos = [key, fuente[key],fecha]
        inserta_tabla_fuente(datos)


# funcion para actualizar toda la tabla consolidada con los datos de provincia y categoría del proyecto
def actualiza_tabla_provincia_categoria(provincia_categoria):
    # crea la tabla (si se encuentra creada la elimina y genera una nueva)
    crea_tabla_provincia_categoria()
    fecha = str(date.today())
    for key in provincia_categoria:
        row = str(key)
        row = row.split(" - ")
        datos = [row[0],row[1],provincia_categoria[key],fecha]
        inserta_tabla_provincia_categoria(datos)


# funcion para actualizar toda la tabla consolidada con los datos de los cines del proyecto
def actualiza_tabla_cine(cine):
    # crea la tabla (si se encuentra creada la elimina y genera una nueva)
    crea_tabla_cine()
    fecha = str(date.today())
    for row in cine:
        datos = [row[0],row[1],row[2],row[3],fecha]
        inserta_tabla_cine(datos)

