import matplotlib as plt
import scrutins as scr

class Election :
    def __init__(self, nom, dates, candidats, electeurs, mode ):
        self._nom = nom
        self._debut = dates[0]
        self._fin = dates[1]
        self.__candidats = candidats
        self.__electeurs = electeurs
        if mode in ["condorcet","Condorcet"]:
            self.scrutin = scr.Condorcet(candidats)
        elif mode in ["Jugement majoritaire", "jugement majoritaire"] :
            self.scrutin = scr.Jugement_majoritaire(candidats)
        else :
            print("Le scrutin demandé n'est pas pris en charge !")
        self.__urne = []

    def verifs_elec(self, candidat):
        return 42

    def read_cand(self):
        return 42

    def disp_cand(self):
        return 42

    def depouillage(self):
        return 42

    def disp_results(self):
        return 42

class Bulletin :
    def __init__(self, election):
        self.id = len(election.geturne())
        self.validite = True









