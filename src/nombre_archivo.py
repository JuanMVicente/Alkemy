from datetime import date
import os


def monthName(num):
    # Diccionario que permite pasar de número a texto el mes correspondiente
    dict = {
        1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',
        7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'
    }
    return dict[num]


def completeNum(num):
    # Permite dar formato al número
    if num<10:
        return "0"+ str(num)
    else:
        return str(num)


def nombre(category):
    # Genera la carpeta de la categoría
    if not(os.path.isdir(category)):
            os.mkdir(category)
    dt = date.today()
    # Crea la carpeta correspondiente al mes
    nameLocation = category + "\\" + str(dt.year) + "-" + monthName(dt.month)
    nameFile = nameLocation + "\\" + category + "-" + completeNum(dt.day) + "-" + completeNum(dt.month) + "-" + str(dt.year) + ".csv"
    if not(os.path.isdir(nameLocation)):
        os.mkdir(nameLocation)
    return nameFile


def direccion(category):
    # Devuelve la direccion del ultimo archivo de la categroría (por ahora no lo uso)
    # tiene la limitacion que entre carpeta con el ultimo mes vigente y puede no estar generado
    dt = date.today()
    direccion = os.getcwd() + category + "\\" + str(dt.year) + "-" + monthName(dt.month)
    return direccion
