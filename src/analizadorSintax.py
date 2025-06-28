import ply.yacc as yacc
from analizadorLex import tokens, build_lexer
from sem import symbol_table, addSymbol, printTable, inferIDType, inferNumericType, unifyTypes, isVariableTypeCompatibleWithVarType, inferTypeFromToken




lexer = build_lexer()

errores = []

start = 'program'


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


def p_statement(p):
    '''statement : expression SEMICOLON
                 | declaration
                 | assignation
                 | assignation_no_type
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
                 | list
                 | set
                 | map
                 | empty'''


def p_declaration(p):
    'declaration : varType ID SEMICOLON'
    # Puede almacenar la variable sin valor, si deseas



def p_assignation(p):
    'assignation : varType ID ASSIGN_OPERATOR variable SEMICOLON'
    variableType = p[4]
    name = p[2]
    varType = p[1]
    print(f"[assignation] Declarando {name} como {varType} con valor tipo {variableType}")

    if isVariableTypeCompatibleWithVarType(varType, variableType):
        addSymbol(name, variableType)
        printTable()
    else:
        print(f"ERROR. No se puede asignar '{variableType}' a '{varType}'")
        printTable()



def p_assignation_no_type(p):
    'assignation_no_type : ID ASSIGN_OPERATOR variable SEMICOLON'
    name = p[1]
    valueType = p[3]
    prevType = inferIDType(name)

    if prevType is None:
        print(f"[assignation] ERROR: variable '{name}' no declarada")
    elif not isVariableTypeCompatibleWithVarType(prevType, valueType):
        print(f"[assignation] ERROR: tipo incompatible '{valueType}' para '{prevType}'")
    else:
        print(f"[assignation] Asignando valor '{valueType}' a variable existente '{name}'")

def p_expression_operations(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    print(f"[expression] Unificando {p[1]} con {p[3]}")
    p[0] = unifyTypes(p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_operations(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | term MODULE factor'''
    print(f"[term] Unificando {p[1]} con {p[3]}")
    p[0] = unifyTypes(p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_numeric(p):
    '''factor : INT
              | DOUBLE'''
    print(f"[numeric] token: {p.slice[1].type}, value: {p[1]}")
    p[0] = inferNumericType(p[1])

def p_variable(p):
    '''variable : INT 
                | DOUBLE 
                | STRING 
                | BOOL  
                | NULL
                | ID
                | expression'''
    token = p.slice[1].type
    var = p[1]
    if token in ['INT', 'DOUBLE', 'STRING', 'BOOL', 'NULL']:
        p[0] = inferTypeFromToken(token)
    elif token == "ID":
        tipo = inferIDType(var)
        if tipo is None:
            print(f"[variable] ERROR: variable '{var}' no definida")
        p[0] = tipo
    else:
        p[0] = p[1]



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
    p[0] = p[1]



def p_boolean_expression(p):
    '''booleanExpression : variable EQUALS variable
                         | variable NOT_EQUALS variable
                         | variable GREATER_THAN variable
                         | variable LESS_THAN variable
                         | variable GREATER_THAN_OR_EQUALS variable
                         | variable LESS_THAN_OR_EQUALS variable'''
    p[0] = 'bool'

def p_if(p):
    '''if : IF LPARENTHESIS booleanExpression RPARENTHESIS LBRACE statements RBRACE
          | IF LPARENTHESIS booleanExpression RPARENTHESIS LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''

def p_while(p):
    '''while : WHILE LPARENTHESIS booleanExpression RPARENTHESIS LBRACE statements RBRACE'''

def p_for(p):
    '''for : FOR LPARENTHESIS assignation booleanExpression SEMICOLON increment RPARENTHESIS LBRACE statements RBRACE'''

def p_increment(p):
    '''increment : ID INCREMENT'''

def p_print(p):
    'print : PRINT LPARENTHESIS expression RPARENTHESIS SEMICOLON'

def p_input(p):
    'input : ID ASSIGN_OPERATOR STDIN DOT READ LPARENTHESIS RPARENTHESIS SEMICOLON'

def p_class_def(p):
    'class_def : CLASS ID LBRACE class_members RBRACE'

def p_class_members(p):
    '''class_members : class_members class_member
                     | class_member'''

def p_class_member(p):
    '''class_member : varType ID SEMICOLON
                    | function'''

def p_function(p):
    'function : varType ID LPARENTHESIS parameters RPARENTHESIS LBRACE statements RBRACE'


def p_enum(p):
    'enum : ENUM ID LBRACE enum_values RBRACE'

def p_enum_values(p):
    '''enum_values : enum_values COMMA ID
                   | ID'''


def p_try(p):
    'try : TRY LBRACE statements RBRACE FINALLY LBRACE statements RBRACE'


def p_switch(p):
    'switch : SWITCH LPARENTHESIS variable RPARENTHESIS LBRACE cases default_case RBRACE'

def p_cases(p):
    '''cases : cases case
             | case'''

def p_case(p):
    'case : CASE variable COLON statements BREAK SEMICOLON'

def p_default_case(p):
    'default_case : DEFAULT COLON statements'


def p_parameters(p):
    '''parameters : parameters COMMA parameter
                  | parameter
                  | empty'''

def p_parameter(p):
    'parameter : varType ID'

def p_list(p): 'list : empty'  # Temporal
def p_set(p): 'set : empty'
def p_map(p): 'map : empty'

def p_empty(p): 'empty :'

def p_error(p):
    if p:
        error_msg = f"Error de sintaxis en la línea {p.lineno}, token: '{p.value}'"
    else:
        error_msg = "Error de sintaxis: fin inesperado de entrada"
    errores.append(error_msg)
    print(error_msg)

parser = yacc.yacc()

# === Consola interactiva ===
if __name__ == '__main__':
    while True:
        try:
            s = input('dart > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s, lexer=lexer)
        print(result)

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