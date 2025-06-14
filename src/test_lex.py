import ply.lex as lex 
from datetime import datetime
import os

input_folder = "../Algoritmos/"
output_folder = "../Logs/"

# Construcción del lexer
lexer = lex.lex()

for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        lex.input(file_content)

        filename_split = filename.split(".")

        output_path = os.path.join(output_folder, "lexico-" + filename_split[0] + "-" + datetime.now().strftime("%d-%m-%Y-%Hh%M") + ".txt")

        with open(output_path, 'w', encoding='utf-8') as outfile:
            while True:
                tok = lexer.token()
                if not tok:
                    break
                outfile.write(str(tok) + "\n")