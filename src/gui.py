from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, QFrame, QTextEdit
from PyQt5.QtCore import Qt

# def on_button_click():
#     label.setText("Button Clicked!")

# app = QApplication([])

# window = QWidget()
# window.setWindowTitle("Simple PyQt5 GUI")
# window.setGeometry(100, 100, 400, 300)

# label = QLabel("Hello, PyQt5!", window)
# label.move(150, 100)  # This places the label in the window

# button = QPushButton("Click Me", window)
# button.move(150, 150)
# button.clicked.connect(on_button_click)

# window.show()
# app.exec_()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Los galacticos")
        self.setGeometry(100, 100, 1200, 800)
        self.initUI()

    def initUI(self):
        main__container = QWidget(self)
        main__container.setStyleSheet(""" 
        QWidget {
                background-color: #1e2833;
                }
    """)
        self.setCentralWidget(main__container)
        layout = QVBoxLayout(main__container)

        header = QFrame() # es como un div de HMTL
        header.setFixedHeight(150)
        header_layout = QVBoxLayout(header)
        header.setFrameShape(QFrame.StyledPanel)


        title = QLabel("CODE ANALYZER")
        title.setAlignment(Qt.AlignCenter)  # Centra el texto   
        title.setStyleSheet("font-weight: bold; font-size: 24px; color: #c9b977")
    
        participants = QLabel("Group members:")
        participants.setAlignment(Qt.AlignCenter)
        participants.setStyleSheet("font-weight: medium; font-size: 18px; color:#c9b977")

        participant1 = QLabel("Diego Fernando Flores Rengifo")
        participant1.setAlignment(Qt.AlignCenter)
        participant1.setStyleSheet("font-weight: medium; font-size: 12px; color:#9ae5f3")
        
        participant2 = QLabel("Alex Vizuete")
        participant2.setAlignment(Qt.AlignCenter)
        participant2.setStyleSheet("font-weight: medium; font-size: 12px; color:#9ae5f3")
        participant3 = QLabel("Kevin Salazar")
        participant3.setAlignment(Qt.AlignCenter)
        participant3.setStyleSheet("font-weight: medium; font-size: 12px; color:#9ae5f3")

        header_layout.addWidget(title)
        header_layout.addWidget(participants)
        header_layout.addWidget(participant1)
        header_layout.addWidget(participant2)
        header_layout.addWidget(participant3)



        layout.addWidget(header)
        buttons__container = QFrame()
        buttons__container.setFrameShape(QFrame.StyledPanel)
        buttons__container.setStyleSheet("""
        QFrame {
                background-color: #23272f;                           
                padding; 10px;   
            }
        """)
        buttons__container__layout = QHBoxLayout(buttons__container)
        buttons__container__layout.setContentsMargins(0,0,0,0) # elimina los margenes del contenedor
        buttons__container__layout.setSpacing(0)

        left__container = QWidget()
        left__container__layout  = QHBoxLayout(left__container)
        left__container__layout.setAlignment(Qt.AlignCenter)
        left__container__layout.setContentsMargins(0,0,80,0)
        left__container__layout.setSpacing(80)
        

        load__btn = QPushButton("Load File")
        new__file__btn = QPushButton("New File")
        load__btn.setStyleSheet("Padding: 15px 20px;" \
                                "background-color: #2b7ed7;" \
                                "color: #fff; border-radius: 5px")
        new__file__btn.setStyleSheet("Padding: 15px 20px;" \
                                "background-color: #2b7ed7;" \
                                "color: #fff; border-radius: 5px")
        
        left__container__layout.addWidget(load__btn)
        left__container__layout.addWidget(new__file__btn)

        right__container = QWidget()
        right__container__layout = QHBoxLayout(right__container)
        right__container__layout.setContentsMargins(0,0,0,0)
        right__container__layout.setAlignment(Qt.AlignCenter)
        

        run__btn = QPushButton("Run")
        run__btn.setStyleSheet("Padding: 15px 20px;" \
                                "background-color: #2b7ed7;" \
                                "color: #fff; border-radius: 5px")
        right__container__layout.addWidget(run__btn, alignment=Qt.AlignCenter)
        buttons__container__layout.addWidget(left__container)

        buttons__container__layout.addWidget(right__container)
        layout.addWidget(buttons__container)

        body = QFrame()
        body__layout = QHBoxLayout(body)
        body.setFrameShape(QFrame.StyledPanel) # enables to add style to the body
        body.setStyleSheet("""
            QFrame {
                    background-color: #23272f;
                    border: 2px solid #444;           
                }
         """)
        

        body__layout__left__side = QFrame()
        body__layout__left__side.setFrameShape(QFrame.StyledPanel)
        body__layout__left__side.setStyleSheet("""
            QFrame {
                background: #181c23;
                border: 2px solid;
                border-radius: 8px;                                                                              
                }
         """)
        
        left__side__layout = QVBoxLayout(body__layout__left__side)
        self.textbox = QTextEdit()
        self.textbox.setStyleSheet("""
            QTextEdit {
                        background-color: #181c23;
                                   color: #fff;
                                   font-family: 'Consolas', monospace;
                                   font-size: 14px;
                                   border: none;
                                   }
        """)

        body__layout__right__side = QFrame()
        body__layout__right__side.setFrameShape(QFrame.StyledPanel)
        body__layout__right__side.setStyleSheet("""
            QFrame {
                background: #181c23;
                border: 2px solid;
                border-radius: 8px;                                                         
                }
        """)
        left__side__layout.addWidget(self.textbox)
        right__side__layout = QVBoxLayout(body__layout__right__side)
        self.resultbox = QTextEdit()
        self.resultbox.setReadOnly(True)
        self.resultbox.setStyleSheet("""
                QTextEdit {
                    background: #181c23;
                    color: #fff;
                    font-family: Consolas, monospace;
                    font-size: 15px;
                    border: none;
                }
            """)        
        right__side__layout.addWidget(self.resultbox)
      
        body__layout.addWidget(body__layout__left__side)
        body__layout.addWidget(body__layout__right__side)
        layout.addWidget(body, stretch=1)



