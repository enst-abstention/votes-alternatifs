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
        self.__debut = dates[0]
        self.__fin = dates[1]
        self.__candidats = candidats
        self.__electeurs = electeurs
        if mode in ["condorcet", "Condorcet"]:
            self.__scrutin = scr.Condorcet(candidats)
        elif mode in ["Jugement majoritaire", "jugement majoritaire"]:
            self.__scrutin = scr.Jugement_majoritaire(candidats)
        else:
            print("Le scrutin demandé n'est pas pris en charge !")
        self.__urne = []

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
        if electeur in self.__electeurs :
            return True
        else :
            return False

    def remplissage_urne(self, bulletin):
        """
        Permet de placer un bulletin dans l'urne.

        Parameters :
        ______________
        bulletin : dict
            Le bulletin d'un électeur
        """
        self.__urne.append(bulletin)

    def depouillement(self):
        return 42

    def aff_resultats(self):
        print("Le vainqueur de l'élection est {}.".format(self.depouillement()))
        print("\t Pour plus d'information cliquer sur 'afficher les statistiques'.")


class Bulletin:
    def __init__(self, election):
        self.__election = election
        self.__id = 1
        self.__valide = False
        self.__date = datetime.date
        self.__vote = {}

    def complete(self):
        """
        Demande à l'électeur de remplir son bulletin
        """
        print (self.__election.__scrutin.message())


    def estvalide(self):
        """
        Vérifie que le bulletin rempli bien les conditions de validité de l'élection.

        Returns
        _________
        bool :
            True si les conditions sont vérifiées
        """

        testdate = self.__election.debut < self.__date < self.__election.fun
        testelecteur = self.__election.verif_elect(self.__id)
        testcandidats = all(self.__vote.keys()) in self.__election.candidats
        testvote = all(self.__vote.items()) in self.__election.__scrutin.__votes_autorisés

        if all([testdate, testelecteur, testcandidats, testvote]):
            return True
