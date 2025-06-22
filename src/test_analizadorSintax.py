from analizadorSintax import analizar_archivo
from datetime import datetime
from zoneinfo import ZoneInfo
import os

carpeta = '../Algoritmos/'
ruta_errores = '../LogsSintax/'

for archivo in os.listdir(carpeta):
    direccionAlgoritmo = os.path.join(carpeta, archivo)
    
    # Quita la parte inicial y la extensión
    nombreAlgoritmo = archivo.split(".dart")[0]
    fecha = datetime.now(ZoneInfo('America/Guayaquil')).strftime('%d-%m-%Y-%Hh%M')
    direccionLog = f"{ruta_errores}sintactico-{nombreAlgoritmo}-{fecha}.txt"
    
    analizar_archivo(direccionAlgoritmo, direccionLog)