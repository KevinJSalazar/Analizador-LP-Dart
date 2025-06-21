import ply.lex as lex
from datetime import datetime
import os

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'return': 'RETURN',
    'while': 'WHILE',
    'var': 'VAR',
    'const': 'CONST',
    'final': 'FINAL',
    'late': 'LATE',
    'void': 'VOID',
    'enum': 'ENUM',
    'static': 'STATIC',
    'import': 'IMPORT',
    'abstract': 'ABSTRACT',
    'typedef': 'TYPEDEF',
    'break': 'BREAK',
    'default': 'DEFAULT',
    'continue': 'CONTINUE',
    'export': 'EXPORT',
    'finally': 'FINALLY',
    'double': 'DOUBLE_TYPE',
    'int': 'INT_TYPE',
    'num': 'NUM_TYPE',
    'String': 'STRING_TYPE',
    'bool': 'BOOL_TYPE',
    'List': 'LIST_TYPE',
    'Map': 'MAP_TYPE',
    'Set': 'SET_TYPE',
    'null' : 'NULL'
}

# Falta añadir comentarios

tokens = list(reserved.values()) + [
    'COMMENT_LINE', #regex
    'COMMENT_BLOCK', #regex
    'ID', #regex    
    'PLUS', #regex
    'MINUS', #regex
    'DIVIDE', #regex
    'TIMES', #regex
    'AND', #regex
    'OR', #regex
    'NOT', #regex
    'EQUALS', #regex
    'NOT_EQUALS', #regex
    'GREATER_THAN', #regex
    'LESS_THAN', #regex
    'GREATER_THAN_OR_EQUALS', #regex
    'LESS_THAN_OR_EQUALS', #regex
    'BOOL',
    'INT',
    'STRING',
    'DOUBLE',
    'LPARENTHESIS', #regex
    'RPARENTHESIS', #regex
    'SEMICOLON', #regex
    'LBRACE', #regex 
    'RBRACE', #regex
    'DOT', #regex
    'COMMA', #regex
    'COLON', #regex
    'ASSIGN_OPERATOR', #regex,
    'LBRACKET', #regex
    'RBRACKET', #regex,
    'MODULE', #regex
]   


t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_TIMES = r'\*'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT_EQUALS = r'!='
t_NOT = r'!'
t_ASSIGN_OPERATOR = r'='
t_EQUALS = r'=='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_GREATER_THAN_OR_EQUALS = r'>='
t_LESS_THAN_OR_EQUALS = r'<='
t_LPARENTHESIS = r'\('
t_RPARENTHESIS = r'\)'
t_SEMICOLON = r';'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'
t_COMMA = r','
t_COLON = r':'
t_ignore = ' \t'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_MODULE = r'\%'

def t_COMMENT_LINE(t):
    r'//.*'
    return t

def t_COMMENT_BLOCK(t):
    r'/\*[\s\S]*?\*/'
    return t

def t_DOUBLE(t):
    r'\d+.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_BOOL(t):
    r'true|false'
    t.value = bool(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\''
    t.value = t.value[1:-1] 
    return t

def t_new_line(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t    

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)




lexer = lex.lex()

input_folder = "../Algorithms/"
output_folder = "../Logs/"

'''
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
'''








