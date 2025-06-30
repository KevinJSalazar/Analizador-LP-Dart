// Algoritmo de ejemplo para test del analizador léxico
import 'dart:math';

/* Este programa almacena temperaturas,
   las filtra según un umbral y muestra resultados. */

void main() {
  final double threshold = 30.5;
  var temperatures = <double>[28.0, 31.2, 29.5, 32.1, 27.0];
  List<double> highTemps = [];

  for (double temp in temperatures) {
    if (temp > threshold) {
      highTemps.add(temp);
    } else {
      continue; // Temperatura no supera el umbral
    }
  }

  print("Temperaturas altas detectadas:");
  for (var t in highTemps) {
    print("- $t°C");
  }

  final Map<String, bool> estado = {
    "alerta": highTemps.length > 2,
    "estable": highTemps.length <= 2
  };

  print("\nEstado del sistema:");
  estado.forEach((clave, valor) {
    print("$clave: $valor");
  });

  // Declaraciones alternativas
   bool sistemaActivo = true;
  late String mensaje;

  if (sistemaActivo) {
    mensaje = "Sistema operativo en línea.";
  }

  print("\nMensaje: $mensaje");
}

