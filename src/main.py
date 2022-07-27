from actualizar_sql import *
import descarga
from procesamiento_datos import Procesador

def main():
    # descarga.descarga()
    datos = Procesador()
    actualizar_tabla_general(datos.general)
    actualiza_tabla_categoria(datos.totales_categoria)
    actualiza_tabla_fuente(datos.totales_fuente)
    actualiza_tabla_provincia_categoria(datos.totales_provincia_y_categoria)
    actualiza_tabla_cine(datos.totales_cines)
    
    

if __name__ == "__main__":
    main()