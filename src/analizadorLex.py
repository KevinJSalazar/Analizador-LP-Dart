import ply.lex as lex

reserved = {
    # === Palabras clave de control de flujo ===
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    
    'while': 'WHILE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'try': 'TRY',
    'finally': 'FINALLY',

    # === Declaración de variables y constantes ===
    'var': 'VAR',
    'const': 'CONST',
    'final': 'FINAL',
    'late': 'LATE',

    # === Declaración de funciones y clases ===
    'void': 'VOID',
    'class': 'CLASS',
    'static': 'STATIC',
    'abstract': 'ABSTRACT',
    'typedef': 'TYPEDEF',
    'enum': 'ENUM',

    # === Importación y exportación ===
    'import': 'IMPORT',
    'export': 'EXPORT',

    # === Tipos de datos primitivos ===  # Diego Flores
    'double': 'DOUBLE_TYPE',
    'int': 'INT_TYPE',
    'num': 'NUM_TYPE',
    'String': 'STRING_TYPE',
    'bool': 'BOOL_TYPE',
    'true': 'TRUE',
    'false': 'FALSE',
    'null': 'NULL_TYPE',

    # === Estructuras de datos ===  # Alex Vizuete
    'List': 'LIST_TYPE',
    'Set': 'SET_TYPE',
    'Map': 'MAP_TYPE',
    
    # === Entrada/Salida ===
    'print': 'PRINT',
    'stdin': 'STDIN',
    'readLineSync': 'READ',
}

# Tokens generales
tokens = list(reserved.values()) + [
    # Literales y tipos de datos
    'ID',
    'PLUS', 'MINUS', 'DIVIDE', 'TIMES', 'MODULE',
    'INCREMENT', 'DECREMENT',
    'PLUS_EQUALS', 'MINUS_EQUALS', 'TIMES_EQUALS', 'DIVIDE_EQUALS',
    'AND', 'OR', 'NOT',
    'EQUALS', 'NOT_EQUALS',
    'GREATER_THAN', 'LESS_THAN',
    'GREATER_THAN_OR_EQUALS', 'LESS_THAN_OR_EQUALS',
    'BOOL', 'INT', 'DOUBLE', 'STRING', 'NULL',
    # Delimitadores
    'LPARENTHESIS', 'RPARENTHESIS',
    'SEMICOLON', 'LBRACE', 'RBRACE',
    'DOT', 'COMMA', 'COLON',
    'ASSIGN_OPERATOR', 'ARROW',
    'LBRACKET', 'RBRACKET',
    
]

# Operadores y delimitadores
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_PLUS_EQUALS = r'\+='
t_MINUS_EQUALS = r'-='
t_TIMES_EQUALS = r'\*='
t_DIVIDE_EQUALS = r'/='
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_TIMES = r'\*'

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_GREATER_THAN_OR_EQUALS = r'>='
t_LESS_THAN_OR_EQUALS = r'<='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'

t_ASSIGN_OPERATOR = r'='
t_LPARENTHESIS = r'\('
t_RPARENTHESIS = r'\)'
t_SEMICOLON = r';'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOT = r'\.'
t_COMMA = r','
t_COLON = r':'
t_ARROW = r'=>'
t_MODULE = r'%'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Comentarios
def t_ignore_COMMENT_LINE(t):
    r'//.*'

def t_ignore_COMMENT_BLOCK(t):
    r'/\*[\s\S]*?\*/'

# Literales numéricas y booleanas
def t_DOUBLE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BOOL(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
    return t

# Null literal
def t_NULL(t):
    r'null'
    t.value = None
    return t

# Strings entre comillas simples o dobles
def t_STRING(t):
    r'"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\''
    t.value = t.value[1:-1]
    return t

# Control de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

# Identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Errores léxicos
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Función para construir el lexer
def build_lexer():
    return lex.lex()



