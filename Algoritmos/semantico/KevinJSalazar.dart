int x = 5;
bool b = true;

if (b) {           // Correcto
  print("ok");
}

if (x) {           // Error semántico: x no es bool
  print("fail");
}

while (b) {        // Correcto
  x = x + 1;
}

while (x) {        // Error semántico: x no es bool
  x = x + 1;
}

for (int i = 0; b; i++) {   // Correcto
  print(i);
}

for (int i = 0; x; i++) {   // Error semántico: x no es bool
  print(i);
}

if (b && x) {      // Error semántico: x no es bool
  print("fail");
}

List<int> numeros = [1, 2, 3];
Set<String> nombres = {"Ana", "Luis"};
int noColeccion = 10;

for (int n in numeros) {      // Correcto
  print(n);
}

for (String nombre in nombres) { // Correcto
  print(nombre);
}

for (double w in numeros) {   // Error semántico: tipo incompatible
  print(w);
}

for (int y in noColeccion) {  // Error semántico: noColeccion no es colección
  print(y);
}

for (int z in indefinido) {   // Error semántico: indefinido no declarado
  print(z);
}

int opcion = 2;
String letra = "a";
bool bandera = true;

switch (opcion) {           // Correcto
  case 1:
    print("Uno");
    break;
  case 2:
    print("Dos");
    break;
  default:
    print("Otro");
}

switch (letra) {            // Correcto
  case "a":
    print("Letra a");
    break;
  case "b":
    print("Letra b");
    break;
  default:
    print("Otra letra");
}

switch (bandera) {          // Error semántico: tipo no soportado en switch
  case true:
    print("Es true");
    break;
  case false:
    print("Es false");
    break;
  default:
    print("Otro valor");
}

switch (opcion) {           // Error semántico: tipo de case incompatible
  case "uno":
    print("String en switch de int");
    break;
  default:
    print("Default");
}