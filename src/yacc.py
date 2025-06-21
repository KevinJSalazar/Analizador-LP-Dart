import ply.yacc as yacc
from analizadorLex import tokens

def p_variable(p):
    '''variable : INT 
                | DOUBLE 
                | STRING 
                | BOOL  
                | NULL'''
    
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
                | FINAL'''

def p_booleanExpression(p):
    '''booleanExpression : variable EQUALS variable
                        | variable NOT_EQUALS variable
                        | variable GREATER_THAN variable
                        | variable LESS_THAN variable
                        | variable GREATER_THAN_OR_EQUALS variable
                        | variable LESS_THAN_OR_EQUALS variable
                        '''


def p_declaration(p):
    '''declaration : CONST ID ASSIGN_OPERATOR variable SEMICOLON
                     | VAR ID ASSIGN_OPERATOR variable SEMICOLON
                     | FINAL ID ASSIGN_OPERATOR variable SEMICOLON
    '''


def p_error(p):
    print("Syntax error")


parser = yacc.yacc()   

while True:
   try:
       s = input('dart > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)