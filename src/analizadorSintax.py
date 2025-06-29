import ply.yacc as yacc
from analizadorLex import tokens, build_lexer
from analizadorSem import symbol_table, addSymbol, printTable, inferIDType, inferNumericType, unifyTypes, isVariableCompatibleWithVarType, inferTypeFromToken

# =========================
# Configuración y utilidades
# =========================

lexer = build_lexer()
errores = []
errores_semanticos = []
start = 'program'

precedence = (
    ('nonassoc', 'IFX'),   # if sin else
    ('nonassoc', 'ELSE'),  # else se asocia con el último if
)

# =========================
# Programa principal
# =========================

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

# =========================
# Sentencias principales
# =========================

def p_statement_block(p):
    'statement : LBRACE statements RBRACE'
    p[0] = ('block', p[2])

def p_statement(p):
    '''statement : expression SEMICOLON
                 | declaration SEMICOLON
                 | assignation SEMICOLON
                 | increment SEMICOLON
                 | decrement SEMICOLON
                 | import
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
                 | empty
                 | return SEMICOLON
                 | CONTINUE SEMICOLON
                 | BREAK SEMICOLON'''
    
# =========================
# Declaraciones y asignaciones
# =========================
def p_declaration(p):
    '''declaration : declaration_with_modifier
                   | declaration_without_modifier'''
    p[0] = p[1]

def p_declaration_with_modifier(p):
    '''declaration_with_modifier : declaration_modifier varType ID
                                 | declaration_modifier ID'''
    if len(p) == 4:
        print("MATCH: declaration_modifier varType ID")
        p[0] = ('declaration', p[1], p[2], p[3])
    else:
        print("MATCH: declaration_modifier ID")
        p[0] = ('declaration', p[1], None, p[2])

def p_declaration_without_modifier(p):
    'declaration_without_modifier : varType ID'
    print("MATCH: varType ID")
    p[0] = ('declaration', None, p[1], p[2])


# def p_declaration(p): GENERABA CONFLICTO
#     '''declaration : declaration_modifier varType ID 
#                    | declaration_modifier ID 
#                    | varType ID'''
#     if len(p) == 4:
#         print("it mathched format --> declaration_modifier varType ID ")
#         p[0] = ('declaration', p[1], p[2], p[3])
#     elif len(p) == 3:
#         print(f"this is p[1] -> '{p[0]}' ")
#         print(f"this is p[2] -> '{p[1]}' ")
#         print(f"this is p[3] ->  '{p[2]}' ")
#         print("it mathched format --> declaration_modifier ID ")
#         p[0] = ('declaration', p[1], None, p[2])
#     else:
#         print("it mathched format --> varType ID")
#         p[0] = ('declaration', None, p[1], p[2])

def p_declaration_list_init(p):
    '''declaration : LIST_TYPE LESS_THAN varType GREATER_THAN ID ASSIGN_OPERATOR list_literal
                   | declaration_modifier LIST_TYPE LESS_THAN varType GREATER_THAN ID ASSIGN_OPERATOR list_literal'''
    
    if len(p) == 8:
        print("is goes in")
        var_type = p[3]      
        var_name = p[5]      
        list_literal = p[7]  # ('list', [3, 4, 5])
    else:
        var_type = p[4]
        var_name = p[6]
        list_literal = p[8]  # ('list', [...])

    elements = list_literal[1]
    p[0] = ('declaration_list_init', ('List', var_type), var_name, list_literal)

    # Verificación semántica
    line = p.lineno(6)  # donde está el ID
    is_valid = True
    print(f"THIS IS THE STRUCTURE OF ELEMENT '{elements}'")
    for token in elements:
        print(f"TOKEN VALUE '{token}' ")
        if token != var_type:
            print(f"INCOMPATIBILIDAD DE TIPOS")
            is_valid = False
            break
    if is_valid:
        print(f"[OK] Todos los elementos son compatibles con 'List<{var_type}>'")
        addSymbol(var_name, f'List<{var_type}>')
   
    else:
        errores_semanticos.append(
            f"line {line}: cannot assign list with incompatible elements to List<{var_type}>"
        )
    printTable()

 

def p_declaration_other_list_init(p):
    'declaration : declaration ASSIGN_OPERATOR LESS_THAN varType GREATER_THAN list_literal'
    p[0] = ('declaration_other_list_init', p[1], p[4], p[6])

def p_declaration_map_init(p):
    '''declaration : MAP_TYPE LESS_THAN varType COMMA varType GREATER_THAN ID ASSIGN_OPERATOR map_literal
                   | declaration_modifier MAP_TYPE LESS_THAN varType COMMA varType GREATER_THAN ID ASSIGN_OPERATOR map_literal'''
    if len(p) == 10:
        p[0] = ('declaration_map_init', ('Map', p[3], p[5]), p[7], p[9])
    else:
        p[0] = ('declaration_map_init', ('Map', p[4], p[6]), p[8], p[10])

def p_assignation(p):
    'assignation : declaration ASSIGN_OPERATOR variable' ##  varType ID
    print("inside p_assignation")
    declaration = p[1]
    declaration_type = declaration[0]
    line= p.lineno(2)
    variable = p[3]
    if(declaration_type == 'declaration'):
        _, _, varType, variableName = declaration
        print(f"the variable's name is '{variableName}' ")
        print(f"varType is '{varType}' ")
        print(f"the variable type is :'{variable}' ")
        if(isVariableCompatibleWithVarType(varType, variable)):
            addSymbol(variableName, variable) ## se supone que dentro de addSymbol debe de retornar el tipo o se maneja la logica
   
        else:
            print(f"IS NOT POSSIBLE TO ASSIGN '{variable} TO TYPE '{varType}' '")
    elif(declaration_type == 'declaration_list_init'):
        print("THIS IS A LIST")
    elif(declaration_type == 'declaration_other_list_init'):
        print("something")
    elif(declaration_type == 'declaration_map_init'):
        print("any")
    else:
        addError(line)
    printTable
    p[0] = ('assign', p[1], p[2], p[3])




    # def p_list_literal(p):
    #     'list_literal : LBRACKET list_elements RBRACKET'
    #     p[0] = ('list', p[2])


    # def p_declaration_list_init(p):
    # '''declaration : LIST_TYPE LESS_THAN varType GREATER_THAN ID ASSIGN_OPERATOR list_literal
    #                | declaration_modifier LIST_TYPE LESS_THAN varType GREATER_THAN ID ASSIGN_OPERATOR list_literal'''
    # if len(p) == 8:
    #     p[0] = ('declaration_list_init', ('List', p[3]), p[5], p[7])
    # else:
    #     p[0] = ('declaration_list_init', ('List', p[4]), p[6], p[8])


    # def p_list_elements(p):
    # '''list_elements : list_elements COMMA variable
    #                  | variable
    #                  | empty'''
    # if len(p) == 4:
    #     p[0] = p[1] + [p[3]]
    # elif len(p) == 2 and p[1] != None:
    #     p[0] = [p[1]]
    # else:
    #     p[0] = []


def p_assignation_no_type(p):
    'assignation : ID ASSIGN_OPERATOR variable'
    p[0] = ('assign_no_type', p[1], p[3])


def p_compound_assignation(p):
    '''assignation : ID PLUS_EQUALS expression
                   | ID MINUS_EQUALS expression
                   | ID TIMES_EQUALS expression
                   | ID DIVIDE_EQUALS expression'''
    p[0] = ('compound_assign', p[2], p[1], p[3])

def p_declaration_modifier(p):
    '''declaration_modifier : CONST 
                            | FINAL
                            | LATE'''

# =========================
# Tipos de datos
# =========================

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
                 | VOID'''
    p[0] = p[1]
    print(f"hey you just printed the value '{p[1]}'" )

# =========================
# Literales y estructuras de datos
# =========================

def p_list_literal(p):
    'list_literal : LBRACKET list_elements RBRACKET'
    p[0] = ('list', p[2])

def p_list_elements(p):
    '''list_elements : list_elements COMMA variable
                     | variable
                     | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2 and p[1] != None:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_map_literal(p):
    'map_literal : LBRACE map_elements RBRACE'
    p[0] = ('map', p[2])

def p_map_elements(p):
    '''map_elements : map_elements COMMA map_pair
                   | map_pair
                   | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2 and p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_map_pair(p):
    '''map_pair : variable COLON variable
                | variable COLON booleanExpression'''
    p[0] = (p[1], p[3])

# =========================
# Variables y expresiones básicas
# =========================

def p_variable(p):
    '''variable : INT 
                | DOUBLE 
                | STRING 
                | BOOL  
                | NULL
                | ID
                | function
                | lambda
                | expression'''
    token = p.slice[1].type
    if(token in ['INT', 'DOUBLE', 'STRING', 'BOOL', 'NULL']):
        p[0] = inferTypeFromToken(token)
    elif (token == 'ID'):
        p[0] = inferIDType(p[1])    
    else:
        print(token)   
# =========================
# Expresiones aritméticas
# =========================

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

def p_factor_unary_minus(p):
    'factor : MINUS factor'
    p[0] = ('uminus', p[2])

def p_factor_numeric(p):
    '''factor : INT
              | DOUBLE'''
    if isinstance(p[1], int):
        p[0] = ('int', p[1])
    else:
        p[0] = ('double', p[1])

def p_factor_id(p):
    'factor : ID'
    p[0] = ('id', p[1])

def p_factor_parens(p):
    'factor : LPARENTHESIS expression RPARENTHESIS'
    p[0] = p[2]

def p_variable_array_access(p):
    'factor : ID LBRACKET expression RBRACKET'
    p[0] = ('array_access', p[1], p[3])

def p_variable_member_access(p):
    '''factor : ID DOT function statement
              | ID DOT function
              | ID DOT ID'''
    if len(p) == 5:
        p[0] = ('member_call_block', p[1], p[3], p[4])
    else:
        p[0] = ('member_access', p[1], p[3])

# =========================
# Expresiones booleanas
# =========================

def p_boolean_expression_comparison(p):
    '''booleanExpression : variable EQUALS variable
                         | variable NOT_EQUALS variable
                         | variable GREATER_THAN variable
                         | variable LESS_THAN variable
                         | variable GREATER_THAN_OR_EQUALS variable
                         | variable LESS_THAN_OR_EQUALS variable'''
    p[0] = ('boolop', p[2], p[1], p[3])

def p_boolean_expression_logic(p):
    '''booleanExpression : booleanExpression AND booleanExpression
                         | booleanExpression OR booleanExpression'''
    p[0] = ('boolop', p[2], p[1], p[3])

def p_boolean_expression_paren(p):
    'booleanExpression : LPARENTHESIS booleanExpression RPARENTHESIS'
    p[0] = p[2]

def p_boolean_expression_variable(p):
    'booleanExpression : variable'
    p[0] = p[1]

# =========================
# Estructuras de control
# =========================

# If
def p_if(p):
    'if : IF LPARENTHESIS booleanExpression RPARENTHESIS statement %prec IFX'
    p[0] = ('if', p[3], p[5])

def p_if_else(p):
    'if : IF LPARENTHESIS booleanExpression RPARENTHESIS statement ELSE statement'
    p[0] = ('if_else', p[3], p[5], p[7])

# While
def p_while(p):
    'while : WHILE LPARENTHESIS booleanExpression RPARENTHESIS LBRACE statements RBRACE'
    p[0] = ('while', p[3], p[6])

# For clásico y for-in
def p_for(p):
    '''for : FOR LPARENTHESIS assignation SEMICOLON booleanExpression SEMICOLON increment RPARENTHESIS LBRACE statements RBRACE
           | FOR LPARENTHESIS assignation SEMICOLON booleanExpression SEMICOLON decrement RPARENTHESIS LBRACE statements RBRACE'''
    p[0] = ('for', p[3], p[5], p[7], p[10])

def p_for_in(p):
    'for : FOR LPARENTHESIS varType ID IN ID RPARENTHESIS LBRACE statements RBRACE'
    p[0] = ('for_in', p[3], p[4], p[6], p[9])

def p_increment(p):
    'increment : ID INCREMENT'
    p[0] = ('increment', p[1])

def p_decrement(p):
    'decrement : ID DECREMENT'
    p[0] = ('decrement', p[1])

# Try-finally
def p_try(p):
    'try : TRY LBRACE statements RBRACE FINALLY LBRACE statements RBRACE'
    p[0] = ('try_finally', p[3], p[7])


def p_switch(p):
    'switch : SWITCH LPARENTHESIS variable RPARENTHESIS LBRACE cases default_case RBRACE'
    p[0] = ('switch', p[3], p[6], p[7])

def p_cases(p):
    '''cases : cases case
             | case'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_case(p):
    '''case : CASE variable COLON statements BREAK
            | CASE variable COLON statements SEMICOLON
            | CASE variable COLON statements'''
    p[0] = ('case', p[2], p[4])

def p_default_case(p):
    'default_case : DEFAULT COLON statements'
    p[0] = ('default', p[3])

# =========================
# Funciones y parámetros
# =========================

def p_function(p):
    '''function : declaration LPARENTHESIS parameters RPARENTHESIS LBRACE statements RBRACE
                | ID LPARENTHESIS parameters RPARENTHESIS'''

def p_function_arrow(p):
    'function : declaration LPARENTHESIS parameters RPARENTHESIS ARROW expression SEMICOLON'

def p_parameters(p):
    '''parameters : parameters COMMA parameter
                  | parameter
                  | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2 and p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_parameter(p):
    '''parameter : declaration
                 | variable'''
    p[0] = p[1]

def p_lambda(p):
    'lambda : LPARENTHESIS parameters RPARENTHESIS LBRACE statements RBRACE'
    p[0] = ('lambda', p[2], p[5])

# =========================
# Entrada/Salida
# =========================

def p_print(p):
    'print : PRINT LPARENTHESIS variable RPARENTHESIS SEMICOLON'

def p_input(p):
    'input : ID ASSIGN_OPERATOR STDIN DOT READ LPARENTHESIS RPARENTHESIS SEMICOLON'

# =========================
# Clases y objetos
# =========================

def p_class_def(p):
    '''class_def : CLASS ID LBRACE class_members RBRACE'''

def p_class_members(p):
    '''class_members : class_members class_member
                     | class_member'''

def p_class_member(p):
    '''class_member : varType ID SEMICOLON
                    | function'''

# =========================
# Enum y typedef
# =========================

def p_enum(p):
    'enum : ENUM ID LBRACE enum_values RBRACE'

def p_enum_values(p):
    '''enum_values : enum_values COMMA ID
                   | ID'''

def p_typedef(p):
    'typedef : TYPEDEF ID ASSIGN_OPERATOR varType function LPARENTHESIS parameters RPARENTHESIS SEMICOLON'

# =========================
# Sentencias especiales
# =========================

def p_return(p):
    '''return : RETURN variable
              | RETURN'''
    if len(p) == 3:
        p[0] = ('return', p[2])
    else:
        p[0] = ('return', None)

def p_import(p):
    'import : IMPORT STRING SEMICOLON'
    p[0] = ('import', p[2])

def p_empty(p):
    'empty :'
    pass


def p_list(p):
    '''list : '''  # Completa esta regla con la sintaxis esperada para una lista
    pass


def p_set(p):
    '''set : '''  # Define la regla de conjuntos
    pass


def p_map(p):
    '''map : '''  # Define la regla de mapas
    pass

# =========================
# Manejo de errores
# =========================

def p_error(p):
    if p:
        error_msg = f"Error de sintaxis en la línea {p.lineno}, token: '{p.value}'"
    else:
        error_msg = "Error de sintaxis: fin inesperado de entrada"
    errores.append(error_msg)
def addError():
    print(3)
# =========================
# Consola interactiva
# =========================

parser = yacc.yacc()

if __name__ == '__main__':
    print("\n=== Prueba del lexer ===")
    test_lexer = build_lexer()
    test_lexer.input("int x;")
    for token in test_lexer:
        print(f"type: {token.type}, value: {token.value}")
    print("=== Fin de prueba del lexer ===\n")

    while True:
        try:
            s = input('dart > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s, lexer=lexer)
        print(result)


# =========================
# Construcción y análisis
# =========================

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


    #         def p_assignation(p):
    # 'assignation : declaration ASSIGN_OPERATOR variable'
    # p[0] = ('assign', p[1], p[2], p[3])



# def p_declaration_modifier(p):
#     '''declaration_modifier : VAR 
#                             | CONST 
#                             | FINAL'''




def elementsCompatibleWithListType():
    print(2)
