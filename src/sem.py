symbol_table = {
    "variable": {

    },
    "type": {
        "string_type": [],
        "list_type": ["append", "index", "get", "delete"] 
    }

}

def addSymbol (name, type):
   symbol_table["variable"][name] = type

def printTable():
   print(symbol_table)


def unifyTypes(type1, type2):
    pass
      

def inferIDType(variable):
   if(variable in symbol_table["variable"]):
      return symbol_table["variable"][variable]
   else:
      return None
     
# def inferType(variable):
#     if(isinstance(variable, int)):
#       return "int"
#     if(isinstance(variable, float)):
#       return "double"
#     elif(isinstance(variable, str)):
#         return "str"
#     elif(isinstance(variable, bool)):
#         return "bool" 
#     else:
#        return "NULL"

#DID NOT WORK BECAUSE OF INCOMPATIBILITY BETWEEN DART AND PYTHON BOOLEAN VALUES.


def inferTypeFromToken(token_type):
    mapping = {
        'INT': 'int',
        'DOUBLE': 'double',
        'STRING': 'String',
        'BOOL': 'bool',
        'NULL': 'NULL'
    }
    return mapping.get(token_type, 'unknown')

def unifyTypes(type1, type2):
    if(type1 == type2):
       return type1
    else:
        if({type1, type2} == {"int", "double"}):
          return type2
        elif ({type1, type2} == {"double", "int"}):
           return type1
        else:
           print(f" NO se puede unificar '{type1}' con '{type2}' ")
           return None

def inferNumericType(var):
   if(isinstance(var, int)):
      return "int"
   return "double"


def isVariableTypeCompatibleWithVarType(varType, variableType):
    allowed = {
        'int': ['int'],
        'double': ['double'],  
        'String': ['String'],
        'bool': ['bool'],
        'null': ['null'],
    }
    if varType not in allowed:
       return False
    return variableType in allowed[varType]

# def inferPrimitiveType(token):
#     allowed = {
#     'INT_TYPE': 'int',
#     'STRING_TYPE': 'str',
#     'DOUBLE_TYPE': 'double',
#     'BOOL_TYPE': 'bool',
#     'LIST_TYPE': 'List',
#     'MAP_TYPE': 'Map',
#     'VAR': '',
#     'CONST': '',
#     'FINAL' : '',
#     'VOID' : 'VOID',
#    }
#     if(token in allowed):
#         return allowed[token]
#     return None
    

    # int value = 3;
    # bool flag = value;
    

 

