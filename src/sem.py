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
     
def inferType(variable):
    if(isinstance(variable, int)):
      return "int"
    if(isinstance(variable, float)):
      return "double"
    elif(isinstance(variable, str)):
        return "str"
    elif(isinstance(variable, bool)):
        return "bool" 
    else:
       return "NULL"

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

