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
    print(ex)


def crea_tabla_general():
    cursor = connection.cursor()
    query =  '''CREATE TABLE consolidado_general
            (
                cod_localidad varchar(8),
                id_provincia varchar(2),
                id_departamento varchar(6),
                categoria varchar(60),
                provincia varchar(60),
                localidad varchar(50),
                nombre varchar(120),
                domicilio varchar(100),
                cp varchar(10),
                telefono varchar(30),
                mail varchar(100),
                web varchar(150),
                fecha varchar(10)
            );'''
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
    query = 'DROP TABLE consolidado_general'
    cursor.execute(query)
    cursor.close()

def inserta_tabla_general(cod_localidad, id_provincia, id_departamento, categoria, provincia, localidad, nombre, domicilio, cp, telefono, mail, web,fecha):
    cursor = connection.cursor()
    query = f"INSERT INTO consolidado_general values ('{cod_localidad}','{id_provincia}','{id_departamento}','{categoria}','{provincia}','{localidad}','{nombre}','{domicilio}','{cp}','{telefono}','{mail}','{web}','{fecha}')"
    cursor.execute(query)
    cursor.close()

def crea_tabla_categoria():
    cursor = connection.cursor()
    query = '''CREATE TABLE totales_categoria
            (
                categoria varchar(40),
                total int,
                fecha varchar(10)
            );'''
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
    query = 'DROP TABLE totales_categoria'
    cursor.execute(query)
    cursor.close()

def inserta_tabla_categoria(categoria, total,fecha):
    cursor = connection.cursor()
    query = f"INSERT INTO totales_categoria values ('{categoria}',{total},'{fecha}')"
    cursor.execute(query)
    cursor.close()

def crea_tabla_fuente():
    cursor = connection.cursor()
    query = '''CREATE TABLE totales_fuente
            (
                fuente varchar(100),
                total int,
                fecha varchar(10)
            );'''
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
    query = 'DROP TABLE totales_fuente'
    cursor.execute(query)
    cursor.close()

def inserta_tabla_fuente(fuente, total, fecha):
    cursor = connection.cursor()
    query = f"INSERT INTO totales_fuente values ('{fuente}',{total},'{fecha}')"
    cursor.execute(query)
    cursor.close()


def crea_tabla_provincia_categoria():
    cursor = connection.cursor()
    query = '''CREATE TABLE totales_provincia_categoria
            (
                provincia varchar(60),
                categoria varchar(60),
                total int,
                fecha varchar(10)
            );'''
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
    query = 'DROP TABLE totales_provincia_categoria'
    cursor.execute(query)
    cursor.close()

def inserta_tabla_provincia_categoria(categoria, provincia, total,fecha):
    cursor = connection.cursor()
    query = f"INSERT INTO totales_provincia_categoria values ('{categoria}','{provincia}',{total},'{fecha}')"
    cursor.execute(query)
    cursor.close()


def crea_tabla_cine():
    cursor = connection.cursor()
    query = '''CREATE TABLE info_salas_cine
            (
                provincia varchar(60),
                pantallas int,
                butacas int,
                incaa int,
                fecha varchar(10)
            );'''
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
    query = 'DROP TABLE info_salas_cine'
    cursor.execute(query)
    cursor.close()

def inserta_tabla_cine(provincia, pantallas, butacas, incaa, fecha):
    cursor = connection.cursor()
    query = f"INSERT INTO info_salas_cine values ('{provincia}',{pantallas},{butacas},{incaa},'{fecha}')"
    cursor.execute(query)
    cursor.close()
