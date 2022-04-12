class Scrutin :
    def __init__(self,candidats):
        self.candidats = []

    def bulletin_valide(self):
        return
    #def classement(self):
    def statisque(self):
        return

class Condorcet(Scrutin):

    def __init__(self):
        Scrutin.__init__(self,candidats)

    def confrontation_a_deux(self):
        return
    def confrontation_generale(self):
        return
    def afficher_resultats(self):
        return

class Jugement_majoritaire(Scrutin):

    def __init__(self):
        Scrutin.__init__(self, candidats)

    def rangement_candidat(self):
        return
    def mediane(self):
        return
    def afficher_resultat(self):
        return