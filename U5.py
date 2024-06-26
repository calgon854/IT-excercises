import sys
import urllib.parse
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):

        self.setWindowTitle("MainWindow")

        self.resize(375, 250)                       ## damit geoprogrammierung ganz drauf ist wie gefordert

        # Layout erstellen:
        layout = QFormLayout()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        viewmenu = menubar.addMenu("View")

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
        self.countries       = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich", "Polen"])
        self.kartebt         = QPushButton("Karte anzeigen")
        self.ladebt          = QPushButton("Laden")
        self.savebt          = QPushButton("Speichern")

        # Layout füllen:
        layout.addRow("Vorname:", self.vname)
        layout.addRow("Name:", self.name)
        layout.addRow("Geburtstag:", self.geburi)
        layout.addRow("Adresse:", self.addi)
        layout.addRow("Postleitzahl:", self.plz)
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.countries)
        layout.addRow(self.kartebt)
        layout.addRow(self.ladebt)
        layout.addRow(self.savebt)
 
        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

    def createConnects(self):
        self.kartebt.clicked.connect(self.karte)
        self.ladebt.clicked.connect(self.load)
        self.savebt.clicked.connect(self.save)
        self.savemenu.triggered.connect(self.save)
        self.quit.triggered.connect(QApplication.quit)

    def load(self):
        filename, typ = QFileDialog.getOpenFileName(self, "datei öffnen", "", "Alle (*.*);; Text (*.txt)")  #gibt filename zurück und filtert im dialog

        if filename !="":
            datei = open(filename, encoding="utf-8")
            inhalt = datei.read()
            datei.close()

        x = inhalt.split(",")

        print(x)

        # text enthält das Datum als Zeichenkette
        dformat = QLocale().dateFormat(format=QLocale.FormatType.ShortFormat)
        self.geburi.setDate(QDate.fromString(x[2], dformat))

        self.vname.setText(x[0])
        self.name.setText(x[1])
        self.addi.setText(x[3])
        self.plz.setText(x[4])
        self.ort.setText(x[5])
        self.countries.setCurrentText(x[6])

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

    def karte(self):
        vnames      = self.vname.text()
        names       = self.name.text()
        geburis     = self.geburi.text()
        addis       = self.addi.text()
        plzs        = self.plz.text()
        orts        = self.ort.text()
        countries   = self.countries.currentText()
    
        link = f"https://www.google.ch/maps/place/{addis}+{plzs}+{orts}+{countries}"
        QDesktopServices.openUrl(QUrl(link))

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()