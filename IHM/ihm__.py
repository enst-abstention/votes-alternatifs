from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication,QStackedWidget,QWidget
from python_files import elections as ele
from python_files import scrutins as scr
import sys
from python_files.elections import *
from python_files.scrutins import *
# from  elections_sheick import *
# from scrutins_sheick import *
import sqlite3
from PyQt5.QtGui import QPixmap

class Welcome(QDialog):

    def __init__(self):
        super(Welcome,self).__init__()
        loadUi("welcome.ui",self)
        self.pushButton.clicked.connect(self.gotoidentifiants)
        self.pushButton_2.clicked.connect(self.gotocreate)

    def gotoidentifiants(self):
        idenditfiants = Idenditfiants()
        widget.addWidget(idenditfiants)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        createaccount=CreateAccount()
        widget.addWidget(createaccount)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Idenditfiants(QDialog):
    def __init__(self):
        super(Idenditfiants,self).__init__()
        loadUi("Idenditfiants.ui",self)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.gotoeligibility)
        self.pushButton_2.clicked.connect(self.backwelcome)

    def backwelcome(self):
        bienvenue = Welcome()
        widget.addWidget(bienvenue)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoeligibility(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if len(user)==0 or len(password)==0:
            self.label_5.setText("Please fill all the fields")
        else :
            eligibility = Eligibility()
            widget.addWidget(eligibility)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAccount(QDialog):
    def __init__(self):
        super(CreateAccount,self).__init__()
        loadUi("account.ui",self)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.clicked.connect(self.signup)
        self.pushButton_2.clicked.connect(self.backwelcome)

    def backwelcome(self):
        bienvenue = Welcome()
        widget.addWidget(bienvenue)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def signup(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirmpass = self.lineEdit_3.text()
        if len(user) == 0 or len(password) == 0 or len(confirmpass) == 0:
            self.label_5.setText("Please fill all the fields")
        elif confirmpass != password:
            self.label_5.setText("Invalid password")
            modescrutin = ModeScrutin()
            widget.addWidget(modescrutin)
            widget.setCurrentIndex(widget.currentIndex() + 1)

class Eligibility(QDialog):
    def __init__(self):
        super(Eligibility,self).__init__()
        loadUi("eligibilite.ui",self)
        self.pushButton_2.clicked.connect(self.gotofillprofile)
        self.pushButton_3.clicked.connect(self.gotowelcome)


    def gotofillprofile(self):
        fillprofile=FillProfile()
        widget.addWidget(fillprofile)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def gotowelcome(self):
        bienvenue = Welcome()
        widget.addWidget(bienvenue)
        widget.setCurrentIndex(widget.currentIndex()+1)


class FillProfile(QDialog):
    def __init__(self):
        super(FillProfile, self).__init__()
        loadUi("fillprofile.ui", self)
        self.pushButton_2.clicked.connect(self.gotomodescrutin)

    def gotomodescrutin(self):
        modescrutin = ModeScrutin()
        widget.addWidget(modescrutin)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class ModeScrutin(QDialog):
    def __init__(self):
        super(ModeScrutin,self).__init__()
        loadUi("modescrutin.ui",self)
        self.pushButton.clicked.connect(self.gotocondorcet)
        self.pushButton_2.clicked.connect(self.gotojugementmajoritaire)

    def gotocondorcet(self):
        condorcet=Condorcet()
        widget.addWidget(condorcet)
        widget.setCurrentIndex(widget.currentIndex() + 1)




    def gotojugementmajoritaire(self):
        jugement=JugementMajoritaire()
        widget.addWidget(jugement)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class Condorcet(QDialog):
    def __init__(self):
        super(Condorcet,self).__init__()
        loadUi("electioncondorcet.ui",self)
        self.pushButton.clicked.connect(self.gotomodescrutin)
        self.pushButton_2.clicked.connect(self.notification)

    def notification(self):
        electionValider = ElectionValider()
        widget.addWidget(electionValider)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def gotomodescrutin(self):
        modescrutin = ModeScrutin()
        widget.addWidget(modescrutin)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.pushButton.clicked.connect(self.gotomodescrutin)



class JugementMajoritaire(QDialog):
    def __init__(self):
        super(JugementMajoritaire,self).__init__()
        loadUi("jujement_majoritaire.ui",self)
        self.pushButton.clicked.connect(self.gotomodescrutin)
        self.pushButton_2.clicked.connect(self.notification)


    def notification(self):
        electionValider=ElectionValider()
        widget.addWidget(electionValider)
        widget.setCurrentIndex(widget.currentIndex() + 1)



    def gotomodescrutin(self):
        modescrutin = ModeScrutin()
        widget.addWidget(modescrutin)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ElectionValider(QDialog):
    def __init__(self):
        super( ElectionValider,self).__init__()
        loadUi("notification election pris en compte.ui",self)
        self.pushButton.clicked.connect(self.gotoresultat)
        self.pushButton_2.clicked.connect(self.gotomodescrutin)

    def gotomodescrutin(self):
        modescrutin = ModeScrutin()
        widget.addWidget(modescrutin)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def gotoresultat(self):
        resultat = Resultat()
        widget.addWidget(resultat)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Resultat(QDialog):
    def __init__(self):
        super(Resultat, self).__init__()
        loadUi("RESULTAS.ui",self)
        self.pushButton.clicked.connect(self.resultatparcondorcet)
        self.pushButton_2.clicked.connect(self.resultatparjugement)

    def resultatparcondorcet(self):
        resulcondorcet=ResultatCondorcet()
        widget.addWidget(resulcondorcet)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def resultatparjugement(self):
        resuljugement = ResultatJugement()
        widget.addWidget(resuljugement)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class ResultatCondorcet(QDialog):
    def __init__(self):
        super(ResultatCondorcet, self).__init__()
        loadUi("resultat_condorcet.ui",self)
        self.pushButton.clicked.connect(self.gotomodescrutin)

    def gotomodescrutin(self):
        modescrutin = ModeScrutin()
        widget.addWidget(modescrutin)
        widget.setCurrentIndex(widget.currentIndex() + 1)






class ResultatJugement(QDialog):
    def __init__(self):
        super(ResultatJugement, self).__init__()
        loadUi("resultat_jugement_majoritaire.ui", self)
        self.pushButton.clicked.connect(self.gotomodescrutin)

    def gotomodescrutin(self):
        modescrutin = ModeScrutin()
        widget.addWidget(modescrutin)
        widget.setCurrentIndex(widget.currentIndex() + 1)








    
if __name__=='__main__' :
    app = QApplication(sys.argv)
    bienvenue = Welcome()

    widget =QtWidgets.QStackedWidget()
    widget.addWidget(bienvenue)

    widget.setFixedHeight(825)
    widget.setFixedWidth(640)

    widget.show()
    try:
        sys.exit(app.exec_())
    except :
        print("Exciting")
