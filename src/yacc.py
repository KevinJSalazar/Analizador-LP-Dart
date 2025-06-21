import ply.yacc as yacc
from lex import tokens

start = 'statement'

def p_statement(p):
    '''statement : expression
                | list
                | declaration
                | assignation
                | function
                | if
                | while
                | for
                | list'''

def p_assignation(p):
    'assignation : varType ID ASSIGN_OPERATOR variable SEMICOLON'

def p_declaration(p):
    'declaration : varType ID SEMICOLON'

def p_numeric(p):
    '''numeric : INT
               | DOUBLE'''

def p_plusOperation(p):
    'expression : expression PLUS term'
def p_minuxOperation(p):
    'expression : expression MINUS term'
     
def p_expressionTerm(p):
    'expression : term'

def p_termTimes(p):
    'term : term TIMES numeric'

def p_termDivide(p):
    'term : term DIVIDE numeric'
    
def p_termModule(p):
    'term : term MODULE numeric'

def p_termValue(p):
    'term : numeric'

def p_variable(p):
    '''variable : INT 
                | DOUBLE 
                | STRING 
                | BOOL  
                | NULL
                | ID
                | expression
                '''

def p_varType(p):
    '''varType : INT_TYPE 
                | STRING_TYPE 
                | NUM_TYPE 
                | DOUBLE_TYPE 
                | BOOL_TYPE 
                | LIST_TYPE 
                | MAP_TYPE 
                | VAR 
                | CONST 
                | FINAL
                | VOID'''
    
def p_primitive(p):
    '''primitive : INT_TYPE
                | STRING_TYPE
                | NUM_TYPE
                | DOUBLE_TYPE
                | BOOL_TYPE'''
    
def p_booleanExpression(p):
    '''booleanExpression : variable EQUALS variable
                        | variable NOT_EQUALS variable
                        | variable GREATER_THAN variable
                        | variable LESS_THAN variable
                        | variable GREATER_THAN_OR_EQUALS variable
                        | variable LESS_THAN_OR_EQUALS variable
                        '''
def p_if(p):
    '''if : IF LPARENTHESIS booleanExpression RPARENTHESIS LBRACE statement RBRACE
           | IF LPARENTHESIS booleanExpression RPARENTHESIS LBRACE statement RBRACE ELSE LBRACE statement RBRACE
           | IF LPARENTHESIS booleanExpression RPARENTHESIS LBRACE RBRACE'''
    
def p_while(p):
    '''while : WHILE LPARENTHESIS booleanExpression RPARENTHESIS LBRACE statement RBRACE
            | WHILE LPARENTHESIS booleanExpression RPARENTHESIS LBRACE RBRACE'''

def p_for(p):
    '''for : FOR LPARENTHESIS assignation booleanExpression SEMICOLON increment RPARENTHESIS LBRACE statement RBRACE
            | FOR LPARENTHESIS assignation booleanExpression SEMICOLON increment RPARENTHESIS LBRACE RBRACE'''

def p_listIntValues(p):
    '''listIntValue : listIntValue COMMA INT'''

def p_list(p):
    '''list : LIST_TYPE LESS_THAN primitive GREATER_THAN ID ASSIGN_OPERATOR L_LBRACKET listIntValue t_RBRACKET SEMICOLON'''
    
def p_increment(p):
    '''increment : ID PLUS PLUS'''

def p_function(p): 
    'function : varType ID LPARENTHESIS parameters RPARENTHESIS LBRACE statement RBRACE'

def p_parameter(p): 
    '''parameter : varType ID'''

def p_parametersList(p):
    '''parametersList : parameter
                | parameter COMMA parametersList'''
    
def p_parameters(p):
    '''parameters : parametersList
                    | empty'''
    
def p_empty(p) : 
    'empty : '


# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('dart > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)