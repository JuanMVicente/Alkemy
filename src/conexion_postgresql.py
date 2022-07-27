import psycopg2
from decouple import config

try:
    connection = psycopg2.connect(
        host=config('POSTGRESQL_host'),
        port=config('POSTGRESQL_port'),
        user=config('POSTGRESQL_user'),
        password=config('POSTGRESQL_password'),
        database=config('POSTGRESQL_database')
    )
    connection.autocommit = True
    # print("conexion exitosa")
except Exception as ex:
    print("No fue posible la conexión con la base de datos")
    print(ex)


def crea_tabla_general():
    cursor = connection.cursor()
    file =  open("src\scriptsSQL\crea_tabla_general.sql", "r")
    query = file.read()
    
    try:
        cursor.execute(query)
        # print("Tabla General ha sido Generada")
    except:
        # print("La tabla General ya existe")
        elimina_tabla_general()
        crea_tabla_general()
    cursor.close()

def elimina_tabla_general():
    cursor = connection.cursor() 
    file = open("src\scriptsSQL\elimina_tabla_general.sql", "r")
    query = file.read()
    cursor.execute(query)
    cursor.close()

def inserta_tabla_general(datos):
    cursor = connection.cursor()
    file = open("src\scriptsSQL\inserta_tabla_general.sql", "r")
    query = file.read()
    cursor.execute(query, datos)
    cursor.close()

def crea_tabla_categoria():
    cursor = connection.cursor()
    file = open("src\scriptsSQL\crea_tabla_categoria.sql", "r")
    query = file.read()
    try:
        cursor.execute(query)
        # print("Tabla TotalesCategoria ha sido Generada")
    except:
        # print("La tabla TotalesCategoria ya existe")
        elimina_tabla_categoria()
        crea_tabla_categoria()
    cursor.close()

def elimina_tabla_categoria():
    cursor = connection.cursor() 
    file = open("src\scriptsSQL\elimina_tabla_categoria.sql", "r")
    query = file.read()
    cursor.execute(query)
    cursor.close()

def inserta_tabla_categoria(datos):
    cursor = connection.cursor()
    file = open("src\scriptsSQL\inserta_tabla_categoria.sql", "r")
    query = file.read()
    cursor.execute(query,datos)
    cursor.close()

def crea_tabla_fuente():
    cursor = connection.cursor()
    file = open("src\scriptsSQL\crea_tabla_fuente.sql", "r")
    query = file.read()
    try:
        cursor.execute(query)
        # print("Tabla TotalesFuente ha sido Generada")
    except:
        # print("La tabla TotalesFuente ya existe")
        elimina_tabla_fuente()
        crea_tabla_fuente()
    cursor.close()

def elimina_tabla_fuente():
    cursor = connection.cursor() 
    file = open("src\scriptsSQL\elimina_tabla_fuente.sql", "r")
    query = file.read()
    cursor.execute(query)
    cursor.close()

def inserta_tabla_fuente(datos):
    cursor = connection.cursor()
    file = open("src\scriptsSQL\inserta_tabla_fuente.sql", "r")
    query = file.read()
    cursor.execute(query,datos)
    cursor.close()


def crea_tabla_provincia_categoria():
    cursor = connection.cursor()
    file = open("src\scriptsSQL\crea_tabla_provincia_categoria.sql", "r")
    query = file.read()
    try:
        cursor.execute(query)
        # print("Tabla TotalesProvinciaCategoria ha sido Generada")
    except:
        # print("La tabla TotalesProvinciaCategoria ya existe")
        elimina_tabla_provincia_categoria()
        crea_tabla_provincia_categoria()

    cursor.close()

def elimina_tabla_provincia_categoria():
    cursor = connection.cursor() 
    file = open("src\scriptsSQL\elimina_tabla_provincia_categoria.sql", "r")
    query = file.read()
    cursor.execute(query)
    cursor.close()

def inserta_tabla_provincia_categoria(datos):
    cursor = connection.cursor()
    file = open("src\scriptsSQL\inserta_tabla_provincia_categoria.sql", "r")
    query = file.read()
    cursor.execute(query,datos)
    cursor.close()


def crea_tabla_cine():
    cursor = connection.cursor()
    file = open("src\scriptsSQL\crea_tabla_cine.sql", "r")
    query = file.read()
    try:
        cursor.execute(query)
        # print("Tabla InfoSalasDeCine ha sido Generada")
    except:
        # print("La tabla InfoSalasDeCine ya existe")
        elimina_tabla_cine()
        crea_tabla_cine()
    cursor.close()

def elimina_tabla_cine():
    cursor = connection.cursor() 
    file = open("src\scriptsSQL\elimina_tabla_cine.sql", "r")
    query = file.read()
    cursor.execute(query)
    cursor.close()

def inserta_tabla_cine(datos):
    cursor = connection.cursor()
    file = open("src\scriptsSQL\inserta_tabla_cine.sql", "r")
    query = file.read()
    cursor.execute(query,datos)
    cursor.close()
