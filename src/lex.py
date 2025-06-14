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
    'finally': 'FINALLY',
    'double': 'DOUBLE_TYPE',
    'int': 'INT_TYPE',
    'num': 'NUM_TYPE',
    'String': 'STRING_TYPE',
    'bool': 'BOOL_TYPE',
    'List': 'LIST_TYPE',
    'MAP': 'MAP_TYPE'
    
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
    'NULL', #regex
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
    'RBRACKET', #regex
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

data = '''
   import 'dart:math';
    /* Este programa almacena temperaturas 
        las filtra segun un umbal y muestra resultados.*/
       
    void main() {
        final double threshold = 30.5;
        var temperatures <double> = [28.0, 31.2, 29.5, 32.1, 27.0];
        List<double> highTemps = [];

        for(double temp in temperatures) {
            if(temp > threshold) {
                highTemps.add(temp);
            }else{
                continue;
            }
        }
    }

    print("Temperaturas altas detectadas:");
    for(var t in highTemps){
        print(" - $t °C");
        }

    final Map<String, bool> estado = {
        "alerta": highTemps.lenght > 2,
        "estable": highTemps.lenght <= 2
    };
    
    print("\nEstado del sistema:");
    estado.forEach((clave, valor) {
        print("$clave: $valor");
    });

    // Declaraciones alternativas
    const bool sistemaActivo = true;
    late String mensaje;

    if (sistemaActivo) {
        mensaje = "Sistema operativo en línea.";
    }

    print("\nMensaje: $mensaje");

    }

'''

lexer.input(data)


while True:
    tok = lexer.token()
    if not tok: 
        break      
    print(tok)







