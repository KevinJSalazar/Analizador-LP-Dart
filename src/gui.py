from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

def on_button_click():
    label.setText("Button Clicked!")

app = QApplication([])

window = QWidget()
window.setWindowTitle("Simple PyQt5 GUI")
window.setGeometry(100, 100, 400, 300)

label = QLabel("Hello, PyQt5!", window)
label.move(150, 100)  # This places the label in the window

button = QPushButton("Click Me", window)
button.move(150, 150)
button.clicked.connect(on_button_click)

window.show()
app.exec_()
