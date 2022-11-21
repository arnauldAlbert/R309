import socket
import sys
import threading

from PyQt5.QtWidgets import *
from threading import *
from PyQt5.QtCore import *

class Worker(QThread):
    def __init__(self, connection, list):
        super().__init__()
        self.connection = connection
        self.list=list
    def run(self):
        msg = ""
        while msg != "exit" and msg != "bye" :
            msg = self.connection.recv(1024).decode()
            self.list.append(msg)
        self.connection.close()
        return

class MonApp(QMainWindow):


    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.connect = QPushButton("Connecter serveur")
        self.disconnect = QPushButton("Déconnecter")
        self.send = QPushButton("send")
        self.msg = QLineEdit()
        self.quitter = QPushButton("Quitter")
        hostlabel = QLabel("Host :")
        self.host = QLineEdit("127.0.0.1")
        portlabel = QLabel("Port:")
        self.port = QLineEdit("10001")
        pseudolabel = QLabel("pseudo")
        self.pseudo = QLineEdit("")
        self.listV = QListView()
        self.list=[]
        listmodel = QStringListModel(self.list)
        self.listV.setModel(listmodel)
        self.quitter.clicked.connect(self._action_quitter)
        self.connect.clicked.connect(self._action_connecter)
        self.disconnect.clicked.connect(self._action_deconnecter)
        self.send.clicked.connect(self._msg_send)
        self.msg.returnPressed.connect(self._msg_send)

        grid.addWidget(hostlabel,0,0)
        grid.addWidget(self.host,1,0)
        grid.addWidget(portlabel,0,1)
        grid.addWidget(self.port,1,1)
        grid.addWidget(pseudolabel,0,2)
        grid.addWidget(self.pseudo,1,2)
        grid.addWidget(self.connect,2,0)
        grid.addWidget(self.disconnect,2,1)
        grid.addWidget(self.quitter,4,3)
        grid.addWidget(self.send,3,3)
        grid.addWidget(self.listV,5,0,7,4)

        grid.addWidget(self.msg,3,0,1,3)
        self.connection = None
        self.worker = None



    def _action_quitter(self):
        if self.worker.isRunning():
            self.worker.terminate()
        QApplication.exit(0)


    def _action_deconnecter(self):
        self.connection.send("bye".encode())
        self.connection.close()
        self.worker.terminate()
        QMessageBox(text="connection fermée").exec()

    def _action_connecter(self):
        host = self.host.text()
        port = int(self.port.text())
        sock = socket.socket()
        try :
            sock.connect((host,port))
        except ConnectionRefusedError:
            QMessageBox(text="erreur de connection, veuiller verifier car le serveur semble innacessible").exec
        except socket.gaierror:
            QMessageBox(text="erreur nom d'hote invalide").exec()
        else :
            self.connection=sock
            self.connection.send(self.pseudo.text().encode())
            QMessageBox(text="connection établie").exec()
            self.worker = Worker(self.connection, self.list)
            self.worker.start()

    def _msg_send(self):
        msg = self.msg.text()
        if self.connection is not None:
            self.connection.send(msg.encode())
            self.msg.clear()
        else :
            QMessageBox(text="impossible d'envoyer un message, socket fermée.").exec()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    windows = MonApp()
    windows.show()
    app.exec()

