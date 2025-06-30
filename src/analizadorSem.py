symbol_table = {
    "scopes": [{}],  # pila de scopes, el actual es el último
    "type": {
        "string_type": [],
        "list_type": ["append", "index", "get", "delete"]
    }
}

def addSymbol(name, type):
    symbol_table["scopes"][-1][name] = type

def printTable():
    print(symbol_table)

def inferIDType(variable):
    # Busca desde el scope más interno al más externo
    for scope in reversed(symbol_table["scopes"]):
        if variable in scope:
            return scope[variable]
    return None

def pushScope():
    symbol_table["scopes"].append({})

def popScope():
    symbol_table["scopes"].pop()



def inferTypeFromToken(token_type):
    mapping = {
        'INT': 'int',
        'DOUBLE': 'double',
        'STRING': 'String',
        'BOOL': 'bool',
        'NULL': 'null'
    }
    return mapping.get(token_type, 'unknown')


    
def unifyTypes(type1, type2):
    if type1 is None or type2 is None:
        print(f"[unifyTypes] Uno de los tipos es None: {type1}, {type2}")
        return None

    if type1 == type2:
        return type1

    if (type1 == "int" and type2 == "double") or (type1 == "double" and type2 == "int"):
        return "double"

    print(f"[unifyTypes] No se puede unificar '{type1}' con '{type2}'")
    return None

def inferNumericType(var):
    if isinstance(var, int):
        return "int"
    return "double"

def isVariableCompatibleWithVarType(varType, variableType):
    allowed = {
        'int': ['int'],
        'double': ['double', 'int'],  
        'String': ['String'],
        'bool': ['bool'],
        'null': ['null'],
    }
    return varType in allowed and variableType in allowed[varType]


def isDeclared(variableName):
    return variableName in symbol_table["variable"]