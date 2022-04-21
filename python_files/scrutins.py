class Scrutin:
    def __init__(self, candidats):
        self.candidats = candidats

    # def classement(self):
    def statistique(self):
        return

class Condorcet(Scrutin):

    def __init__(self, candidats):
        Scrutin.__init__(self, candidats)
        self.__votesAutorises = [i for i in range(len(candidats)+1)]

    @property
    def votesAutorises(self):
        return self.__votesAutorises

    def confrontation2(self, bulletins):
        """
        Rassemble une liste de bulletins de vote dans une matrice de préférences.
        les "bulletins" devraient être une liste de bulletin, où
        chaque bulletin est une liste de classements.  Pour par exemple,
        s’il y a 3 candidats, chaque bulletin de vote doit être une liste de 3
        numéros correspondant aux candidats.  Les classements les plus petits sont
         meilleurs.
        """

        est_prefere = {}
        n = len(self.candidats)
        for i in range(n):
            for j in range(n):
                est_prefere[i, j] = 0
        for bulletin in bulletins:
            for i in range(n):
                for j in range(n):
                    if bulletin[i] < bulletin[j]:
                        est_prefere[i, j] += 1
        return est_prefere

    def vainqueur_condorcet(self, est_prefere):
        """ Determine le gagnant d'une election en utilisant la methode Schulze ( aussi appellé CSSD).
        'candidats' est de type liste et 'estprefere' un dictionnaire qui a pour cle la liste de candidat [i,j]
        et pour valeur un entier qui represente le nombre de voix du candidat
         i ou j prefere par les electeurs".
        """

        # Confronte les candidats deux par deux et affectent a chaque candidat ses victoires
        marge = {}
        n = len(self.candidats)
        for i in range(n):
            for j in range(n):
                marge[i, j] = est_prefere[i, j] - est_prefere[j, i]

        # Trouve le meilleur chemin de i a j en utilisant l'algorithme de Floyd
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j != k != i:
                        smallest = min(marge[j, i], marge[i, k])
                        if marge[j, k] < smallest:
                            marge[j, k] = smallest

        # Le candidat qui reste invainqu est le gagnant
        vainqueurs = []
        for i in range(n):
            for j in range(n):
                if marge[j, i] > marge[i, j]:
                    break
            else:
                vainqueurs.append(i)
        return vainqueurs

    def confrontation2(self, bulletins):
        """Collect a list of ballots into a preference matrix.  'ballots' should
        be a list of ballots, where each ballot is a list of rankings.  For
        example, if there are 3 candidates, each ballot should be a list of 3
        numbers corresponding to the candidates.  Smaller rankings are better."""
        estprefere = {}
        n = len(self)
        for i in range(n):
            for j in range(n):
                estprefere[i, j] = 0
        for bulletin in bulletins:
            for i in range(n):
                for j in range(n):
                    if bulletin[i] < bulletin[j]:
                        estprefere[i, j] += 1
        return estprefere

    def aff_stats(self):
        return

class JugementMajoritaire(Scrutin):

    def __init__(self, candidats):
        Scrutin.__init__(self, candidats)
        self.limite = 2

    def resultats_candidat(self, bulletins):
        """
        Compte les votes des candidats et par mention
        retourne un dictionnaire ayant pour cle les noms
        des candidats et pour valeur un tableau de vote
        """

        resultats_par_candidat = {
            candidat: [0 for _ in range(20)]
            for candidat in self.candidats
        }
        for bulletin in bulletins:
            for candidat, mention in bulletin.items():
                resultats_par_candidat[candidat][mention] += 1
        return resultats_par_candidat



    def mention_majoritaire(self,resultats_par_candidat):
        resultat = {}
        for candidat, resultat1candidat in resultats_par_candidat.items():
            votes_cumules = 0
            for note, compte_vote in enumerate(resultat1candidat):
                votes_cumules += compte_vote
                if self.limite < votes_cumules:
                    resultat[candidat] = {
                        "mention": note,
                        "score": votes_cumules
                    }
                    break

        return result

    def resultat(self, urne):
        vainqueur = "Arthaud"
        return vainqueur

    def aff_stats(self):
        return
