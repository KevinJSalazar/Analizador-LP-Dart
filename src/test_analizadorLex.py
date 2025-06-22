from analizadorLex import build_lexer
from datetime import datetime
from zoneinfo import ZoneInfo
import os

input_folder = "../Algoritmos/"
output_folder = "../LogsLex/"

for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
    
        lexer = build_lexer()
        lexer.input(file_content)

        filename_split = filename.split(".")
        output_name = f"lexico-{filename_split[0]}-{datetime.now(ZoneInfo('America/Guayaquil')).strftime('%d-%m-%Y-%Hh%M')}.txt"
        output_path = os.path.join(output_folder, output_name)

        with open(output_path, 'w', encoding='utf-8') as outfile:
            while True:
                tok = lexer.token()
                if not tok:
                    break
                outfile.write(str(tok) + "\n")
