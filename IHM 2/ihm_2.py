from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication,QStackedWidget,QWidget
import sys
from python_files.elections import *
from python_files.scrutins import *
# from  elections_sheick import *
# from scrutins_sheick import *
import sqlite3
from PyQt5.QtGui import QPixmap

class PemierePage(QDialog) :

    def __init__(self):
        super(PemierePage,self).__init__()
        loadUi("premierepage.ui",self)
        self.bouton_voter.clicked.connect(self.goto_voter)
        self.bouton_creerelection.clicked.connect(self.goto_creer_election)
        self.bouton_afficherresultat.clicked.connect(self.goto_afficher_resultats)


    def goto_voter(self):
        voter = Voter()
        widget.addWidget(voter)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_creer_election(self):
        creer_election = CreerElection()
        widget.addWidget(creer_election)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_afficher_resultats(self):
        afficher = AfficherResultat
        widget.addWidget(afficher)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Voter(QDialog):
    def __init__(self):
        super(Voter,self).__init__()
        loadUi("voter.ui",self)
        self.bouton_continuer.clicked.connect(self.goto_scrutin)

    def goto_scrutin(self):
        identifiants = self.lineEdit.text()
        mot_de_passe = self.lineEdit_2.text()
        conn = sqlite3.connect("(le nom de la base de donnee)")
        cur = conn.cursor()
        query = 'SELECT mot_de_passe from (nom de la table) where identifiants=\''+identifiants+'\''
        cur.execute(query)
        result_pass = cur.fetchone()[0]
        if result_pass == mot_de_passe  : # Le code risque de pas fonctionner a cause de cette partie
            if #mode de scrutin condorcet : # parce que je sais pas quel nom tu as donne a ta base de donnee
                condorcet = Condorcet()
                widget.addWidget(condorcet)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            else :
                jujement = JujementMajoritaire()
                widget.addWidget(jujement)
                widget.setCurrentIndex(widget.currentIndex() + 1)
        else :
            self.label_4.setText("Idendifiants incorrects: vous n'êtes pas autoriser à voter !")


class CreerElection(QDialog) :
    def __init__(self):
        super(CreerElection,self).__init__()
        loadUi("CREER.ui",self)
        self.bouton_creer_election.clicked.connect(self.goto_notif_elec_bien_creer)

    def goto_notif_elec_bien_creer(self):
        notif = NotifElectCreer()
        widget.addWidget(notif)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class  NotifElectCreer(QDialog):
    def __init__(self):
        super(NotifElectCreer, self).__init__()
        loadUi("election bien creer.ui", self)
        self.bouton_continuer.clicked.connect(self.goto_premierepage)

    def goto_premierepage(self):
        bienvenue = PemierePage()
        widget.addWidget(bienvenue)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class AfficherResultat(QDialog):
    def __init__(self):
        super(AfficherResultat, self).__init__()
        loadUi("RESULTATS.ui", self)
        self.bouton_continuer.clicked.connect(self.goto_premierepage)

    def goto_premierepage(self):
        bienvenue = PemierePage()
        widget.addWidget(bienvenue)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Condorcet(QDialog):
    def __init__(self):
        super(Condorcet,self).__init__()
        loadUi("electioncondorcet.ui",self)
        self.bouton_deposer_urne.clicked.connect(self.goto_notif_elect_pris_compte)
        self.bouton_retour.clicked.connect(self.goto_premierepage)

    def goto_notif_elect_pris_compte(self):
        notif2 = NotifPrisCompte()
        widget.addWidget(notif2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_premierepage(self):
        bienvenue = PemierePage()
        widget.addWidget(bienvenue)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class JujementMajoritaire(QDialog):
    def __init__(self):
        super(JujementMajoritaire,self).__init__()
        loadUi("jujement_majoritaire.ui",self)
        self.bouton_deposer_urne.clicked.connect(self.goto_notif_elect_pris_compte)
        self.bouton_retour.clicked.connect(self.goto_premierepage)


    def goto_notif_elect_pris_compte(self):
        notif2 = NotifPrisCompte()
        widget.addWidget(notif2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def goto_premierepage(self):
        bienvenue = PemierePage()
        widget.addWidget(bienvenue)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class NotifPrisCompte(QDialog):
    def __init__(self):
        super(NotifPrisCompte,self).__init__()
        loadUi("notification election pris en compte.ui",self)
        self.bouton_valider.clicked.connect(self.goto_premierepage)
        self.bouton_annuler.clicked.connect(self.goto_voter)

    def goto_premierepage(self):
        bienvenue = PemierePage()
        widget.addWidget(bienvenue)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def goto_voter(self):
        def goto_voter(self):
            voter = Voter()
            widget.addWidget(voter)
            widget.setCurrentIndex(widget.currentIndex() + 1)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    bienvenue = PemierePage()

    widget = QtWidgets.QStackedWidget()
    widget.addWidget(bienvenue)

    widget.setFixedHeight(540)
    widget.setFixedWidth(616)

    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exciting")