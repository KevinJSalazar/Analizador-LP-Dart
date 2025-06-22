import ply.yacc as yacc
from analizadorLex import tokens, build_lexer

lexer = build_lexer()
# Aquí se guardan los errores
errores = []
start = 'program'

# Programa compuesto de múltiples sentencias
def p_program(p):
    '''program : statements'''
    p[0] = ('program', p[1])

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

# Sentencias principales
def p_statement(p):
    '''statement : expression SEMICOLON
                 | declaration
                 | assignation
                 | function
                 | if
                 | while
                 | for
                 | print
                 | input
                 | class_def
                 | enum
                 | try
                 | switch
                 | empty'''

# Declaración
def p_declaration(p):
    'declaration : varType ID SEMICOLON'

# Asignación
def p_assignation(p):
    'assignation : varType ID ASSIGN_OPERATOR variable SEMICOLON'

def p_assignation_no_type(p):
    'assignation : ID ASSIGN_OPERATOR variable SEMICOLON'

# Tipos de datos
def p_varType(p):
    '''varType : INT_TYPE 
               | STRING_TYPE 
               | NUM_TYPE 
               | DOUBLE_TYPE 
               | BOOL_TYPE 
               | LIST_TYPE 
               | MAP_TYPE 
               | SET_TYPE
               | VAR 
               | CONST 
               | FINAL 
               | VOID'''

# Variables y expresiones básicas
def p_variable(p):
    '''variable : INT
                | DOUBLE
                | STRING
                | BOOL
                | NULL
                | ID
                | expression'''

# Expresiones aritméticas
def p_expression_operations(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_operations(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | term MODULE factor'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_numeric(p):
    '''factor : INT
              | DOUBLE'''
    p[0] = ('num', p[1])

# Expresiones booleanas
def p_boolean_expression(p):
    '''booleanExpression : variable EQUALS variable
                         | variable NOT_EQUALS variable
                         | variable GREATER_THAN variable
                         | variable LESS_THAN variable
                         | variable GREATER_THAN_OR_EQUALS variable
                         | variable LESS_THAN_OR_EQUALS variable
                         | booleanExpression AND booleanExpression
                         | booleanExpression OR booleanExpression'''
    if len(p) == 4:
        p[0] = ('boolop', p[2], p[1], p[3])
    else:
        p[0] = p[1]

# Estructuras de control
def p_if(p):
    '''if : IF LPARENTHESIS booleanExpression RPARENTHESIS LBRACE statements RBRACE
          | IF LPARENTHESIS booleanExpression RPARENTHESIS LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''

def p_while(p):
    '''while : WHILE LPARENTHESIS booleanExpression RPARENTHESIS LBRACE statements RBRACE'''

def p_for(p):
    '''for : FOR LPARENTHESIS assignation booleanExpression SEMICOLON increment RPARENTHESIS LBRACE statements RBRACE
           | FOR LPARENTHESIS assignation booleanExpression SEMICOLON decrement RPARENTHESIS LBRACE statements RBRACE'''

def p_increment(p):
    '''increment : ID INCREMENT'''

def p_decrement(p):
    '''decrement : ID DECREMENT'''

# Funciones
def p_function(p):
    'function : varType ID LPARENTHESIS parameters RPARENTHESIS LBRACE statements RBRACE'

def p_function_arrow(p):
    'function : varType ID LPARENTHESIS parameters RPARENTHESIS ARROW expression SEMICOLON'

# Tipedef
def p_typedef(p):
    'typedef : TYPEDEF ID ASSIGN_OPERATOR varType function LPARENTHESIS parameters RPARENTHESIS SEMICOLON'

# Enum
def p_enum(p):
    'enum : ENUM ID LBRACE enum_values RBRACE'

def p_enum_values(p):
    '''enum_values : enum_values COMMA ID
                   | ID'''

# Try-finally
def p_try(p):
    'try : TRY LBRACE statements RBRACE FINALLY LBRACE statements RBRACE'

# Switch-case
def p_switch(p):
    'switch : SWITCH LPARENTHESIS variable RPARENTHESIS LBRACE cases default_case RBRACE'

def p_cases(p):
    '''cases : cases case
             | case'''

def p_case(p):
    'case : CASE variable COLON statements BREAK SEMICOLON'

def p_default_case(p):
    'default_case : DEFAULT COLON statements'

# Parámetros
def p_parameters(p):
    '''parameters : parameters COMMA parameter
                  | parameter
                  | empty'''

def p_parameter(p):
    'parameter : varType ID'

# Entrada/Salida
def p_print(p):
    'print : PRINT LPARENTHESIS expression RPARENTHESIS SEMICOLON'

def p_input(p):
    'input : ID ASSIGN_OPERATOR STDIN DOT READ LPARENTHESIS RPARENTHESIS SEMICOLON'

# Clases y objetos
def p_class_def(p):
    '''class_def : CLASS ID LBRACE class_members RBRACE'''

def p_class_members(p):
    '''class_members : class_members class_member
                     | class_member'''

def p_class_member(p):
    '''class_member : varType ID SEMICOLON
                    | function'''

# Empty
def p_empty(p):
    'empty :'
    pass

# Errores
def p_error(p):
    if p:
        error_msg = f"Error de sintaxis en la línea {p.lineno}, token: '{p.value}'"
    else:
        error_msg = "Error de sintaxis: fin inesperado de entrada"
    errores.append(error_msg)

# Función para construir el parser
def build_parser():
    return yacc.yacc()

def analizar_archivo(ruta_codigo, ruta_errores):
    lexer = build_lexer()   # crea un lexer nuevo
    parser = build_parser() # crea un parser nuevo

    global errores
    errores = []            # limpia errores acumulados
    with open(ruta_codigo, 'r', encoding='utf-8') as f:
        codigo = f.read()
    parser.parse(codigo, lexer=lexer)
    
    with open(ruta_errores, 'w', encoding='utf-8') as f:
        if errores:
            for e in errores:
                f.write(e + '\n')
        else:
            f.write("No se encontraron errores de sintaxis.\n")