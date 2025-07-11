# Analizador-LP-Dart

Proyecto de Lenguajes de Programación - Grupo 11

## Descripción general

Este repositorio contiene un analizador para Lenguajes de Programación desarrollado en Python, que incluye componentes léxicos, sintácticos y semánticos. Utiliza la librería `ply` para el análisis léxico/sintáctico y una interfaz gráfica basada en PyQt5.

## Estructura del proyecto

- **Algoritmos/**: Carpeta destinada a almacenar implementaciones de algoritmos relacionados con el análisis.
- **LogsLex/**: Almacena los registros de ejecución del análisis léxico.
- **LogsSintax/**: Contiene los registros del análisis sintáctico.
- **LogsSemantic/**: Guarda los registros del análisis semántico.
- **src/**: Aquí se encuentra el código fuente principal del proyecto (analizadores, interfaz, etc.).
- **requirements.txt**: Lista de dependencias Python necesarias para ejecutar el proyecto.

## Instalación y ejecución

1. **Clona el repositorio**
   ```sh
   git clone https://github.com/KevinJSalazar/Analizador-LP-Dart.git
   cd Analizador-LP-Dart
   ```

2. **Instala las dependencias**
   Es recomendable usar un entorno virtual:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Ejecuta el proyecto**
  
   ```sh
   cd src
   python main.py
   ```


## Notas adicionales

- Los logs generados durante la ejecución se almacenan en las carpetas correspondientes (`LogsLex`, `LogsSintax`, `LogsSemantic`).
- La interfaz gráfica requiere tener instalado el entorno de escritorio adecuado para PyQt5.

---

