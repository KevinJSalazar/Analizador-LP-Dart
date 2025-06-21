from analizadorLex import tokens
from analizadorSintax import build_parser
from datetime import datetime
import os

# Crear instancia del parser
parser = build_parser()

input_folder = "../Algoritmos/"
output_folder = "../LogsSintax/"

for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    if os.path.isfile(file_path) and filename.endswith(".dart"):
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        # Generar nombre del log
        filename_split = filename.split(".")
        timestamp = datetime.now().strftime('%d-%m-%Y-%Hh%M')
        log_name = f"sintactico-{filename_split[0]}-{timestamp}.txt"
        log_path = os.path.join(output_folder, log_name)

        with open(log_path, 'w', encoding='utf-8') as log_file:
            try:
                result = parser.parse(file_content)
                if result is None:
                    log_file.write("Análisis completado sin errores sintácticos.\n")
                else:
                    log_file.write(f"Resultado del análisis: {result}\n")
            except SyntaxError as e:
                log_file.write(f"Error de sintaxis: {str(e)}\n")
            except Exception as e:
                log_file.write(f"Excepción inesperada: {str(e)}\n")
