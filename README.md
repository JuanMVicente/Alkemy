EJECUCION EL PROGRAMA
.\src\main.py
Una vez ejecutado el programa se descargaran en la carpeta donde se guarde el proyecto, las carpetas con los
archivos descargados, según lo solicitado en el Challenge.

CREACION DEL ENTORNO VENV
virtualenv -p python3 venv
.\venv\Scripts\activate.bat

INSTACION DE DEPENDENCIAS NECESARIAS
pip install requests
pip install psycopg2
pip install python-dotenv python-decouple
pip list para comprobar que los mismos se hayan instalado

CONFIGURACION DE BASE DE DATOS
Base de Datos en PostgreSQL
crear un archivo ".env" en la carpeta de principal que incluya los siguientes datos
POSTGRESQL_host=
POSTGRESQL_port=
POSTGRESQL_user=
POSTGRESQL_password=
POSTGRESQL_database=