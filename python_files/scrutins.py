class Scrutin:
    def __init__(self, candidats):
        self.candidats = candidats

    def bulletin_valide(self):
        return

    # def classement(self):
    def statistique(self):
        return


class Condorcet(Scrutin):

    def __init__(self, candidats):
        Scrutin.__init__(self, candidats)

    def vainqueur_condorcet(self, estprefere):
        """Determine the winner of an election using the Schulze method (sometimes
        called CSSD).  'candidates' should be a list of candidates and 'prefer'
        should be a dictionary that maps the pair (i, j) to the number of voters
        who prefer candidate i to candidate j."""

        # Compute the margin of victory for each candidate i over candidate j.
        margin = {}
        n = len(self)
        for i in range(n):
            for j in range(n):
                margin[i, j] = estprefere[i, j] - estprefere[j, i]

        # Find the strength of the beatpath from j to k using the Floyd algorithm.
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j != k != i:
                        smallest = min(margin[j, i], margin[i, k])
                        if margin[j, k] < smallest:
                            margin[j, k] = smallest

        # Any candidate who remains unbeaten is a winner.
        vainqueurs = []
        for i in range(n):
            for j in range(n):
                if margin[j, i] > margin[i, j]:
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

    def aff_resultats(self):
        return


class JugementMajoritaire(Scrutin):

    def __init__(self, candidats):
        Scrutin.__init__(self, candidats)

    def rangement_candidat(self):
        return

    def afficher_resultat(self):
        return

    def results_hash(self, bulletins):
        """ Count votes per candidate and per mention
        Returns a dict of candidate names containing vote arrays.
        """
        resultats_par_candidat = {
            candidat: [0 for _ in range(20)]
            for candidat in self
        }
        for bulletin in bulletins:
            for candidat, mention in bulletin.items():
                resultats_par_candidat[candidat][mention] += 1
        return resultats_par_candidat

    def majoritary_mentions_hash(self,resultats_par_candidat):
        result = {}
        for candidat, resultat1candidat in resultats_par_candidat.items():
            votes_cumules = 0
            for note, compte_vote in enumerate(resultat1candidat):
                votes_cumules += compte_vote
                if self.__limmed < votes_cumules:
                    result[candidat] = {
                        "mention": note,
                        "score": votes_cumules
                    }
                    break
        return result
