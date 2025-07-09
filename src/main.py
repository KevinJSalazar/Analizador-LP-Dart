import sys 
from PyQt5.QtWidgets import QApplication
from gui import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow() # analizador_dar_gui contiene la ventana principal de la aplicacion
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()