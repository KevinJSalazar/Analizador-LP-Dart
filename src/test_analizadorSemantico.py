from analizadorLex import build_lexer
from analizadorSintax import parser, errores_semantico, log_semantico  # ← importante
from datetime import datetime
from zoneinfo import ZoneInfo
import os

carpeta = '../Algoritmos/semantico/'
ruta_errores = '../LogsSemantic/'

# Asegura que el directorio de logs exista
os.makedirs(ruta_errores, exist_ok=True)

for archivo in os.listdir(carpeta):
    if archivo.endswith(".dart"):
        direccionAlgoritmo = os.path.join(carpeta, archivo)

        # Extrae el nombre base del archivo sin extensión
        nombreAlgoritmo = archivo.split(".dart")[0]
        # fecha = datetime.now(ZoneInfo('America/Guayaquil')).strftime('%d-%m-%Y-%Hh%M')
        direccionLog = f"{ruta_errores}semantico-{nombreAlgoritmo}.txt"

        # Limpiar logs antes de analizar
        errores_semantico.clear()
        log_semantico.clear()

        # Leer código fuente
        with open(direccionAlgoritmo, 'r', encoding='utf-8') as f:
            codigo = f.read()

        # Ejecutar análisis
        lexer = build_lexer()
        parser.parse(codigo, lexer=lexer)

        # Guardar resultados
        with open(direccionLog, 'w', encoding='utf-8') as f:
            if log_semantico:
                f.write("=== VALID EXPRESSIONS ===\n")
                for l in log_semantico:
                    f.write(l + '\n')

            if errores_semantico:
                f.write("\n=== SEMANTIC ERRORS ===\n")
                for e in errores_semantico:
                    f.write(e + '\n')
            else:
                f.write("\nNo se detectaron errores semánticos.\n")

        print(f"✅ Log generado: {direccionLog}")
