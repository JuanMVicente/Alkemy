# diccionario utilizado para facilitar la descarga de datos desde la web
categorys = {
    "Museos": 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv',
    "Salas de Cine" : 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv',
    "Bibliotecas Populares" : 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
    }


# Funcion generada sin utilizar, para cambiar la URL en caso de ser necesario
def cambiarURL(categoria,URL):
    if categoria in categorys:
        categorys[categoria] = URL