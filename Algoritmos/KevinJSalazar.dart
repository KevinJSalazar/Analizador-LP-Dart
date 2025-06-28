// typedef Operacion = int Function(int, int);

enum Estado { activo, inactivo }

void main() {
    const limite = 3;
    var contador = 0;
    final String nombre = 'Carlos';

    while (contador < limite) {
        if (contador == 1) {
            contador++;
            continue;
        }
        print("Contador: $contador");
        contador++;
    }

    for (var i = 0; i < 2; i++) {
        print("Iteración: $i");
    }

    try {
        var resultado = dividir(10, 0);
        print("Resultado: $resultado");
    } finally {
        print("Fin del programa.");
    }
}

int dividir(int a, int b) {
    switch (b) {
        case 0:
            return -1;
        default:
            return a / b;
    }
}