from datetime import date
from conexion_postgresql import crea_tabla_categoria, crea_tabla_cine, crea_tabla_fuente, crea_tabla_general, crea_tabla_provincia_categoria, inserta_tabla_categoria, inserta_tabla_cine, inserta_tabla_fuente, inserta_tabla_general, inserta_tabla_provincia_categoria
from nombre_archivo import completeNum

def actualizar_tabla_general(general):
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
        inserta_tabla_general(row[0],row[1],row[2],row[3],row[4],localidad,nombre,direccion,row[8],row[9],row[10],row[11],fecha)


def actualiza_tabla_categoria(categoria):
    crea_tabla_categoria()
    fecha = str(date.today())
    for key in categoria:
        inserta_tabla_categoria(key, categoria[key],fecha)


def actualiza_tabla_fuente(fuente):
    crea_tabla_fuente()
    fecha = str(date.today())
    for key in fuente:
        inserta_tabla_fuente(key, fuente[key],fecha)


def actualiza_tabla_provincia_categoria(provincia_categoria):
    crea_tabla_provincia_categoria()
    fecha = str(date.today())
    for key in provincia_categoria:
        row = str(key)
        row = row.split(" - ")
        inserta_tabla_provincia_categoria(row[0],row[1],provincia_categoria[key],fecha)

def actualiza_tabla_cine(cine):
    crea_tabla_cine()
    fecha = str(date.today())
    for row in cine:
        inserta_tabla_cine(row[0],row[1],row[2],row[3],fecha)

