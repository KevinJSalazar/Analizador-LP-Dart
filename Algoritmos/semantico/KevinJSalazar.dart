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