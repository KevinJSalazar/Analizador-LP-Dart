import ply.lex as lex

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
    'finally': 'FINALLY'
}

# Falta añadir comentarios

tokens = list(reserved.values()) + [
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
    'NULL', #regex
    'LPARENTHESIS', #regex
    'RPARENTHESIS', #regex
    'SEMICOLON', #regex
    'LBRACE', #regex 
    'RBRACE', #regex
    'DOT', #regex
    'COMMA', #regex
    'COLON', #regex
]


t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_TIMES = r'\*'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT_EQUALS = r'!='
t_NOT = r'!'
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
t_ignore = ' /'



def t_INT(t):
    r'\d+'
    t.value = int(t.value)    
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

data = '''
3 + 4 * 10
  + -20 *2
'''

lexer.input(data)


while True:
    tok = lexer.token()
    if not tok: 
        break      
    print(tok)







