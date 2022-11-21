import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *

def ajouter():
    text2.setText(f"Bonjour {text.text()}")
    QMessageBox(text="bonjour").exec()

def actionquitter():
    QApplication.exit(0)

app = QApplication(sys.argv)
root = QWidget()
root.resize(400,600)
root.setWindowTitle("ma première application")
root.autoFillBackground()
grid = QGridLayout()
root.setLayout(grid)
text = QLineEdit("")
text2 = QLabel("")
bouton = QPushButton("envoyer")
bouton.clicked.connect(ajouter)
affichage = QLabel("saisir")
affichage2= QListView()
list= ["bonjour","salut","hello","guten tag","sayonara"]
listmodel = QStringListModel(list)
#listmodel.insertRow(0)
#listmodel.setData(listmodel.index(0),"bonjour")
affichage2.setModel(listmodel)
affichage2.flow()
boutonquitter = QPushButton("quitter")
boutonquitter.clicked.connect(actionquitter)

grid.addWidget(affichage,0,0)
grid.addWidget(text,0,1)
grid.addWidget(text2,2,1)
grid.addWidget(bouton,1,1)
grid.addWidget(affichage2,1,0,5,1)
grid.addWidget(boutonquitter,1,2)
root.show()


if __name__=="__main__":
    sys.exit(app.exec())