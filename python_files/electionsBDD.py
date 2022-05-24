import datetime
import os.path

import matplotlib as plt
import scrutins as scr
from consolemenu import *
from consolemenu.items import *
import sqlite3 as sql
from random import choices
from string import *

"""module elections :

Ce module permet la création d'une élection avec tous les outils dont elle a besoin.
Il est composé de plusieurs classes : Election, Bulletin, ...
"""


def generation_mdp(length):
    mdp = ""
    return mdp.join(choices(ascii_letters + digits + punctuation, k=length))

def initEtat(bdd):
    con = sql.connect(bdd)
    cur = con.cursor()
    requete = "UPDATE Electeur SET etat=1"
    cur.execute(requete)
    con.commit()
    cur.close()
    con.close()

def recupCandidats(bdd):
    con = sql.connect(bdd, uri=True)
    cur = con.cursor()
    requete_candidats = "SELECT nom FROM Candidats"
    candidatsList = [i[0] for i in cur.execute(requete_candidats).fetchall()]
    cur.close()
    con.close()
    return candidatsList



class ListeElectorale():
    def __init__(self, name):
        self.__name = name
        self.__bdd = sql.connect(os.path.join("", "bdd", "{}.db".format(self.__name)), uri=True)
        self.__cursor = self.__bdd.cursor()
        self.cursor.execute("""create table Electeurs(
            id integer primary key autoincrement unique, 
            prenom varchar(30), nom varchar(30) NOT NULL, 
            mdp varchar(20) NOT NULL, 
            contact varchar(80) NOT NULL, 
            autorisation integer NOT NULL, 
            etat integer NOT NULL);""")
        self.__bdd.commit()

    @property
    def name(self):
        return self.__name

    @property
    def bdd(self):
        return self.__bdd

    @property
    def cursor(self):
        return self.__cursor

    def ajout_electeur(self):
        """
        Auteur : Jérémy LEMAITRE
        """
        print("Renseignez un nouvel électeur :")
        prenom = input("\n \t Prénom :")
        nom = input("\n \t Nom :")
        mdp = generation_mdp(18)
        contact = input("\n \t Email :")
        data = {"prenom": prenom, "nom": nom, "mdp": mdp, "contact": contact, "autorisation": 1, "etat": 0}
        self.cursor.execute("""INSERT INTO Electeurs(prenom, nom, mdp, contact, autorisation, etat) VALUES(:prenom, 
        :nom, :mdp, :contact, :autorisation, :etat)""", data)
        self.__bdd.commit()


class Election:
    """
    Auteur : Jérémy LEMAITRE
    Description : La classe Election permet de définir une unique élection avec les
    paramètres et variables qui lui sont propre.

    Attributes
    ______________

    """

    def __init__(self, nom, dates, electionBDD, mode):
        self.__nom = nom
        if dates[0] <= dates[1]:
            self.__debut = dates[0]
            self.__fin = dates[1]
        else:
            self.__debut = dates[1]
            self.__fin = dates[0]
        self.__bdd = os.path.join("..", "BDDs", "{}".format(electionBDD))
        initEtat(self.__bdd)
        self.__candidats = recupCandidats(self.bdd)
        if mode in ["condorcet", "Condorcet"]:
            self.__scrutin = scr.Condorcet(self.candidats)
        elif mode in ["Jugement majoritaire", "jugement majoritaire"]:
            self.__scrutin = scr.JugementMajoritaire(self.candidats)
        else:
            raise ValueError("Le scrutin demandé n'est pas pris en charge !")

        self.__urne = []
        self.__nbBulletin = 0

    @property
    def nom(self):
        return self.__nom

    @property
    def debut(self):
        return self.__debut

    @property
    def fin(self):
        return self.__fin

    @property
    def bdd(self):
        return self.__bdd

    @property
    def candidats(self):
        return self.__candidats

    @property
    def scrutin(self):
        return self.__scrutin

    @property
    def nbBulletins(self):
        return self.__nbBulletin

    @property
    def urne(self):
        return self.__urne

    def verif_elec(self, idE, mdp):
        """
        Vérifie que si un électeur entré en paramètre est bien présent dans la liste électorale

        Parameters
        ____________
        electeur : str
            Identifiant de l'électeur considéré

        Returns
        ___________
        bool
            True si l'électeur a le droit de voter, False sinon
        """
        con = sql.connect(self.__bdd, uri=True)
        cur = con.cursor()
        requete = "SELECT idElecteur, mdp, autorisation, etat FROM Electeurs WHERE idElecteur={}".format(idE)
        infos = cur.execute(requete).fetchone()
        con.close()
        if not infos:
            return False
        if infos[1] != mdp:
            return False
        if not infos[2] :
            return False
        if infos[3] :
            print("Vous avez déjà voté !")
            return False
        return True

    def remplissage_urne(self, bulletin):
        """
        Permet simplement de placer un bulletin dans l'urne si celui-ci est valide. (Peut-être inutile)

        Parameters :
        ______________
        bulletin : dict
            Le bulletin d'un électeur
        """
        if bulletin.estvalide():
            self.__urne.append(bulletin)
        else:
            print("Vote non pris en compte. Le bulletin n'est pas valide.")

    def vote_en_cours(self):
        """
        Permet de lancer l'élection et de la maintenir jusqu'à la date de cloture. Lorsqu'un nouvel électeur se
        présente, il entre son numéro d'électeur et peut alors accéder au remplissage de son bulletin.
        Le bulletin
        """
        while datetime.datetime.now() < self.fin:
            e = input("Entrer votre numéro d'électeur")
            b = Bulletin(self, e)
            b.complete()
            self.remplissage_urne(b)

    def depouillement(self):
        """
        Une fois que le vote est cloturé, cette fonction appelle la méthode resultat du mode de scrutin choisi. Par
        polymorphisme la méthode traite les bulletins en accord avec le mode de scrutin choisi.

        Returns
        ______________
        vainqueur : str
            Le gagnant de l'élection
        """
        vainqueur = self.scrutin.resultat(self.__urne)
        return vainqueur

    def aff_resultats(self):
        """
        Méthode qui permet l'affichage des résulats de l'élection dans la console Python.
        """
        print("Le vainqueur de l'élection est {}.".format(self.depouillement()))
        print("\t Pour plus d'information cliquer sur 'afficher les statistiques'.")


class Bulletin:
    """
    Auteur : Jérémy LEMAITRE
    Description : Représente le bulletin qu'un électeur rempli et dépose dans l'urne.
    """
    tps = datetime.datetime.now()

    def __init__(self, election, idElecteur, mdp, t=tps):
        self.__election = election
        self.__id = 1000 + election.nbBulletins
        self.__idElecteur = idElecteur
        self.__mdp = mdp
        self.__valide = False
        self.__date = t
        self.__bulletin = {}
        self.rempli = False
        self.candidats_options = {j: election.candidats[j] for j in range(len(election.candidats))}
        self.votes_options = {i: election.scrutin.votesautorises[i] for i in
                              range(len(election.scrutin.votesautorises))}

    @property
    def election(self):
        return self.__election

    @property
    def id(self):
        return self.__id

    @property
    def valide(self):
        return self.__valide

    @property
    def date(self):
        return self.__date

    @property
    def bulletin(self):
        return self.__bulletin

    def print_candidats(self):
        """
        Permet l'affichage des candidats que les électeurs peuvent renseigner sur leur bulletin.
        """
        print("Les candidats sont :\t")
        for key in self.candidats_options.keys():
            print(key, "--", self.candidats_options[key])

    def print_options(self):
        """
        Permet l'affichage des différents choix de vote qui s'offrent aux candidats.
        """
        print("Les options de votes sont :\n")
        for key in self.votes_options.keys():
            print(key, "--", self.votes_options[key])

    def ligne(self):
        """
        Demande à l'électeur de remplir une unique ligne du bulletin et propose les candidats et options de vote

        Returns
        ____________
        candidat : str
            nom du candidat à placer dans le bulletin

        choix : str
            classement, mention ou note attribué au candidat précédemment choisi
        """
        self.print_candidats()
        candidat = input("Entrez le nom d'un candidat :")
        self.print_options()
        vote = input("Entrez le classement associé :")
        estrempli = input("\n Entrez 'y' si votre bulletin est complètement rempli :")
        if estrempli == "y":
            self.rempli = True
        return candidat, vote

    def complete(self):
        """
        Itère le remplissage des lignes et demande à l'électeur s'il a fini de remplir son bulletin.
        Sort de la fonction lorsque le bulletin est rempli
        """
        while not self.rempli:
            candidat, vote = self.ligne()
            self.__bulletin[candidat] = vote

    def estvalide(self):
        """
        Vérifie que le bulletin remplit bien les conditions de validité de l'élection en procédant à plusieurs tests.

        Returns
        _________
        bool :
            True si les conditions sont vérifiées
        """

        testdate = self.election.debut < self.__date < self.election.fin
        testelecteur = self.election.verif_elec(self.__idElecteur,self.__mdp)
        testcandidats = all([(key in self.election.candidats) for key in self.__bulletin.keys()])
        testvote = all([(item in self.election.scrutin.votesautorises) for item in self.__bulletin.values()])
        if all([testdate, testelecteur, testcandidats, testvote]):
            self.__valide = True
            con = sql.connect(self.election.bdd, uri=True)
            cur = con.cursor()
            requete = "UPDATE Electeurs SET etat=1 WHERE idElecteur={}".format(self.__idElecteur)
            cur.execute(requete)
            con.commit()
            cur.close()
            con.close()

        return self.__valide


if __name__ == '__main__':
    # ouverture = datetime.datetime(2022, 4, 10)
    # cloture = datetime.datetime(2022, 4, 25)
    # presid = Election("Élections présidentielles", (ouverture, cloture),
    #                   ["Macron", "Le Pen", "Mélenchon", "Zemmour", "Péceresse", "Jadot", "Lassalle", "Roussel",
    #                    "Dupont-Aignan", "Hidalgo", "Poutou", "Arthaud"], [i for i in range(100)], "condorcet")
    # presid2 = Election("Élections présidentielles", (cloture, ouverture),
    #                    ["Macron", "Le Pen", "Mélenchon", "Zemmour", "Péceresse", "Jadot", "Lassalle", "Roussel",
    #                     "Dupont-Aignan", "Hidalgo", "Poutou", "Arthaud"], [i for i in range(100)],
    #                    "jugement majoritaire")
    # v = Bulletin(presid2, 1)
    # v.complete()
    # print(v.bulletin)

    liste_electorale = ListeElectorale("Presi")
