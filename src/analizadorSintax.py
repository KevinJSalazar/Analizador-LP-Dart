import ply.yacc as yacc
from analizadorLex import tokens

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
                 | empty'''

# Declaración
def p_declaration(p):
    'declaration : varType ID SEMICOLON'

# Asignación
def p_assignation(p):
    'assignation : varType ID ASSIGN_OPERATOR variable SEMICOLON'

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
            | term DIVIDE factor'''
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
    '''for : FOR LPARENTHESIS assignation booleanExpression SEMICOLON increment RPARENTHESIS LBRACE statements RBRACE'''

def p_increment(p):
    '''increment : ID PLUS PLUS'''

# Funciones
def p_function(p):
    'function : varType ID LPARENTHESIS parameters RPARENTHESIS LBRACE statements RBRACE'

# Función tipo flecha
def p_function_arrow(p):
    'function : varType ID LPARENTHESIS parameters RPARENTHESIS ARROW expression SEMICOLON'

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
        print(f"Syntax error at token '{p.value}', line {p.lineno}")
        with open('logs/sintactico-kevin-21062025-17h30.txt', 'a') as f:
            f.write(f"Syntax error at token '{p.value}', line {p.lineno}\n")
    else:
        print("Syntax error at EOF")

# Build parser
parser = yacc.yacc()
