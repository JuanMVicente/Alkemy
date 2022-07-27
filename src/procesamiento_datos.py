
import categorias
import nombre_archivo
import csv

# Se utiliza la clase procesador para realizar el procesamiento de los archivos, generando la consolidacion corresondiente la información
# para ello no se utilizó la librería Panda
class Procesador:
    general = []
    totales_categoria = {'Museos':0, 'Salas de cine':0, 'Bibliotecas Populares':0}
    totales_fuente = {}
    totales_provincia_y_categoria = {}
    totales_cines = []
    totales_cines_aux = {}
    aux_cines = 0

    # contructor con el cual se generan todas las tablas solicitadas para el proyecto
    def __init__(self):
        self.procesa_archivo()


    # procesa cada linea leída en cada uno de los archivos descargados
    def procesa_linea(self,categoria):
        archivo_csv = nombre_archivo.nombre(categoria)
        with open(archivo_csv,mode="r", encoding='UTF8') as archivo:
            lector = csv.reader(archivo, delimiter=",")
            next(lector, None)
            lista = []
            for linea in lector:
                if 'Salas' in linea[4]:
                    self.contador_cines(linea)
                    fila = [linea[0], linea[1], linea[2], linea[4], linea[5], linea[7], linea[8], linea[9], linea[11],linea[12]+linea[13], linea[14], linea[15]]
                elif 'Bibliotecas' in linea[4]:
                    fila = [linea[0], linea[1], linea[2], linea[4], linea[6], linea[8], linea[9], linea[10], linea[12], linea[13]+linea[14], linea[15], linea[16]]
                else:
                    fila = [linea[0], linea[1], linea[2], linea[4], linea[6], linea[7], linea[8], linea[9], linea[11], linea[12]+linea[13], linea[14], linea[15]] 
                lista.append(fila)
                self.contador_categoria(fila)
                self.contador_fuente(linea)
                self.contador_provincia_y_categoria(fila)
        return lista


    # Envía a procesar cada una de las categorías del proyecto
    def procesa_archivo(self):
        categorys = categorias.categorys
        for category in categorys:
            self.general.extend(self.procesa_linea(category))
        return
        
    
    # Realiza los calculos para generar el diccionario con las cantidades de cada una de las categorías
    def contador_categoria(self, fila):
        if fila[3] == 'Espacios de Exhibición Patrimonial':
            self.totales_categoria['Museos'] += 1
        elif fila[3] == 'Salas de cine':
            self.totales_categoria['Salas de cine'] += 1
        elif fila[3] == 'Bibliotecas Populares':
            self.totales_categoria['Bibliotecas Populares'] += 1
        return
    

    # Realiza los calculos para generar el diccionario con las cantidades de cada una de las fuentes
    def contador_fuente(self,linea):
        if linea[21] in self.totales_fuente.keys():
            self.totales_fuente[linea[21]]+=1
        else:
            self.totales_fuente[linea[21]]=1
        return
    

    # Realiza los calculos para generar el diccionario con las cantidades de cada una de las provincias y categorías
    def contador_provincia_y_categoria(self,fila):
        nombre = fila[4] + " - " + fila[3]
        if nombre in self.totales_provincia_y_categoria.keys():
            self.totales_provincia_y_categoria[nombre]+=1
        else:
            self.totales_provincia_y_categoria[nombre]=1
        return
    
    # Realiza los calculos para generar la lista con las cantidades solicitadas de los datos de los cines
    def contador_cines(self,linea):
        # uso un diccionario auxiliar para no agregar lineas de mas en la tabla
        # con la ubicacion de la prov armo la tabla correspondiente
        if linea[22] == "":
            pantallas = 0
        else: 
            pantallas = int(linea[22])
        if linea[23] == "":
            butacas = 0
        else: 
            butacas = int(linea[23])

        if linea[5] in self.totales_cines_aux.keys():
            j = self.totales_cines_aux[linea[5]]
            self.totales_cines[j][1] += pantallas
            self.totales_cines[j][2] += butacas
            if linea[24].upper() == 'SI':                 
                self.totales_cines[j][3] += 1

        else:
            self.totales_cines_aux[linea[5]] = self.aux_cines
            j = self.aux_cines
            self.aux_cines += 1
            if linea[24].upper() == 'SI':               
                INCAA = 1
            else:
                INCAA = 0
            linea_aux = [linea[5], pantallas, butacas, INCAA]
            self.totales_cines.append(linea_aux)
        return

    
# utilizado para prueba/debug de cada una de las funciones
'''utilizado para probar la clase
proc.genera_tabla()
print(proc.datos[0])
print(proc.datos[1000])
print(proc.datos[1500])
print(proc.datos[1800])
print(proc.totales_categoria)
print(proc.totales_fuente)
print(proc.totales_provincia_y_categoria)
print(proc.totales_cines)'''

'''p = Procesador()
print("### tabla de datos ###")
print(p.general[0])
print(p.general[1000])
print(p.general[1500])
print("### totales categoria ###")
print(p.totales_categoria)
print("### totales fuente ###")
print(p.totales_fuente)
print("### totales provincia y categoria ###")
print(p.totales_provincia_y_categoria)
print("### totales cines ###")
print(p.totales_cines)'''