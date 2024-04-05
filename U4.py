import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):

        self.setWindowTitle("GUI-Programmierung")

        self.resize(370, 250)                       ## damit geoprogrammierung ganz drauf ist wie gefordert

        # Layout erstellen:
        layout = QFormLayout()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        self.savemenu = QAction("Save", self)
        self.quit = QAction("Quit", self)

        self.quit.setMenuRole(QAction.QuitRole)   # Rolle "beenden" zuweisen, nur für MacOS relevant

        filemenu.addAction(self.savemenu)
        filemenu.addSeparator()
        filemenu.addAction(self.quit)

        # Widget-Instanzen erstellen:

        self.vname           = QLineEdit()
        self.name            = QLineEdit()
        self.geburi          = QDateEdit()
        self.addi            = QLineEdit()
        self.plz             = QLineEdit()
        self.ort             = QLineEdit()
        self.savebt          = QPushButton("Save")
        self.countries       = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich", "Polen"])


##-------------- Default werte damits der vorgabe entspricht


        self.vname.setText("Alexandra")
        self.name.setText("Müller")
        self.geburi.setDate(QDate(1992, 4, 7))
        self.addi.setText("Hofackerstrasse 30")
        self.plz.setText("4132")
        self.ort.setText("Muttenz")

        # Layout füllen:
        layout.addRow("Vorname:", self.vname)
        layout.addRow("Name:", self.name)
        layout.addRow("Geburtstag:", self.geburi)
        layout.addRow("Adresse:", self.addi)
        layout.addRow("Postleitzahl:", self.plz)
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.countries)
        layout.addRow(self.savebt)
 
        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

    def createConnects(self):
        self.savebt.clicked.connect(self.save)
        self.savemenu.triggered.connect(self.save)
        self.quit.triggered.connect(QApplication.quit)

    def save(self):
        vnames      = self.vname.text()
        names       = self.name.text()
        geburis     = self.geburi.text()
        addis       = self.addi.text()
        plzs        = self.plz.text()
        orts        = self.ort.text()
        countries   = self.countries.currentText()

        line = f"{vnames},{names},{geburis},{addis},{plzs},{orts},{countries}"

        file = open("output.txt",  "w+", encoding="utf-8")              ###utf 8 damit österreich korrekt gespeichert wird
        file.write(line)
        file.close()




def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()