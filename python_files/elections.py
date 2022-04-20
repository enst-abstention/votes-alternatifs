import datetime
import matplotlib as plt
import scrutins as scr

"""module elections :

Ce module permet la création d'une élection avec tous les outils dont elle a besoin.
Il est composé de plusieurs classes : Election, Bulletin, ...
"""


class Election:
    """
    La classe Election permet de définir une unique élection avec les paramètres et variables qui lui sont propre.

    Attributes
    ______________

    """

    def __init__(self, nom, dates, candidats, electeurs, mode):
        self.__nom = nom
        if dates[0] <= dates[1]:
            self.__debut = dates[0]
            self.__fin = dates[1]
        else:
            self.__debut = dates[1]
            self.__fin = dates[0]
        self.__candidats = candidats
        self.__electeurs = electeurs
        if mode in ["condorcet", "Condorcet"]:
            self.__scrutin = scr.Condorcet(candidats)
        elif mode in ["Jugement majoritaire", "jugement majoritaire"]:
            self.__scrutin = scr.JugementMajoritaire(candidats)
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

    def verif_elec(self, electeur):
        """
        Parameters
        ____________
        electeur : str
            Identifiant de l'électeur considéré

        Returns
        ___________
        bool
            True si l'électeur a le droit de voter, False sinon
        """
        if electeur in self.__electeurs:
            return True
        else:
            return False

    def remplissage_urne(self, bulletin):
        """
        Permet de placer un bulletin dans l'urne.

        Parameters :
        ______________
        bulletin : dict
            Le bulletin d'un électeur
        """
        while datetime.datetime.now() < self.fin :
            b = Bulletin(self)
            self.__urne.append(b)

    def depouillement(self):
        vainqueur = self.scrutin.resultat(self.__urne)
        return vainqueur

    def aff_resultats(self):
        print("Le vainqueur de l'élection est {}.".format(self.depouillement()))
        print("\t Pour plus d'information cliquer sur 'afficher les statistiques'.")


class Bulletin:
    def __init__(self, election):
        self.__election = election
        self.__id = 1000 + election.nbBulletins
        self.__valide = False
        self.__date = datetime.datetime.now()
        self.__vote = {}
        self.rempli = False

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

    def ligne(self):
        """
        Demande à l'électeur de remplir son bulletin
        """
        candidat = input("Entrez le nom d'un candidat :")
        choix = input("Entrez le classement associé :")
        return candidat, choix

    def complete(self):
        while not self.rempli :
            candidat, choix = self.ligne()
            self.__vote[candidat] = choix

    def estvalide(self):
        """
        Vérifie que le bulletin remplit bien les conditions de validité de l'élection en procédant à plusieurs tests.

        Returns
        _________
        bool :
            True si les conditions sont vérifiées
        """

        testdate = self.__election.debut < self.__date < self.__election.fun
        testelecteur = self.__election.verif_elect(self.__id)
        testcandidats = all([key in self.__election.candidats for key in self.__vote.keys()])
        testvote = all([item in self.__election.__scrutin.__votesAutorises for item in self.__vote.items()])

        if all([testdate, testelecteur, testcandidats, testvote]):
            return True


if __name__ == '__main__':
    ouverture = datetime.datetime(2022, 4, 10)
    cloture = datetime.datetime(2022, 4, 25)
    presid = Election("Élections présidentielles", (ouverture, cloture),["Macron", "Le Pen", "Mélenchon", "Zemmour", "Péceresse", "Jadot", "Lassalle", "Roussel", "Dupont-Aignan", "Hidalgo", "Poutou", "Arthaud"], [i for i in range(100)], "condorcet")
    presid2 = Election("Élections présidentielles", (cloture, ouverture), ["Macron", "Le Pen", "Mélenchon", "Zemmour", "Péceresse", "Jadot", "Lassalle", "Roussel", "Dupont-Aignan", "Hidalgo", "Poutou", "Arthaud"], [i for i in range(100)],"jugement majoritaire")
    print(presid.aff_resultats())
    print(presid2.aff_resultats())
