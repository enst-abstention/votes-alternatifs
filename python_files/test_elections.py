import sqlite3

from elections import *
from scrutins import *
import unittest
from unittest.mock import patch
import datetime


class TestElection(unittest.TestCase):
    """
    Auteur : Jérémy LEMAITRE
    Description : Cette classe teste les méthodes de la classe Election
    """
    def setUp(self):
        """
        Définition des instances utiles pour l'ensemble de la classe de test.
        """
        ouverture = datetime.datetime(2022, 4, 10)
        cloture = datetime.datetime(2022, 4, 25)
        self.presid = Election("Élections présidentielles", (ouverture, cloture),
                               ["Macron", "Le Pen", "Mélenchon", "Zemmour", "Péceresse", "Jadot", "Lassalle", "Roussel",
                                "Dupont-Aignan", "Hidalgo", "Poutou", "Arthaud"], [i for i in range(100)], "condorcet")
        self.presid2 = Election("Élections présidentielles", (cloture, ouverture),
                                ["Macron", "Le Pen", "Mélenchon", "Zemmour", "Péceresse", "Jadot", "Lassalle",
                                 "Roussel", "Dupont-Aignan", "Hidalgo", "Poutou", "Arthaud"], [i for i in range(100)],
                                "jugement majoritaire")

    def testInit(self):
        """
        Vérifie que les variables d'instance déclarées dans le constructeur sont du type souhaité. Vérifie également
        que la date d'ouverture précède bien la date de cloture. Le constructeur procède à l'inversion des deux dates
        si ce n'est pas le cas.
        """
        self.assertIsInstance(self.presid, Election)
        self.assertIsInstance(self.presid.nom, str)
        self.assertIsInstance(self.presid.debut, datetime.datetime)
        self.assertIsInstance(self.presid.fin, datetime.datetime)
        self.assertIsInstance(self.presid.candidats, list)
        self.assertIsInstance(self.presid.scrutin, Condorcet)
        # self.assertRaises(self.presid.elec, AttributeError)
        # self.assertRaises(self.presid.urne, AttributeError)
        self.assertTrue(self.presid.debut <= self.presid.fin, "La date de cloture précède la date d'ouverture")
        self.assertTrue(self.presid2.debut <= self.presid2.fin, "La date de cloture précède la date d'ouverture")

    def testValideElect(self):
        """
        Vérifie si la fonction verif_elec retourne False quand l'électeur n'est pas dans la liste des électeurs (ici
        pour 1001) et True quand il y est (ici 48).
        """
        valide = self.presid.verif_elec(48)
        invalide = self.presid.verif_elec(1004)
        self.assertTrue(valide)
        self.assertFalse(invalide)

    ########################################################################
    #Ne fonctionne pas comment renseigner les inputs dans les tests unittest
    def testRemplissage(self):
        vote = Bulletin(self.presid, 1)
        b = vote.complete()
        self.presid.remplissage_urne(b)
        self.assertIsInstance(self.presid.urne[-1], dict)
    #########################################################################

class TestBulletin(unittest.TestCase):
    """
    Auteur : Jérémy LEMAITRE
    Description : Cette classe teste les méthodes de la classe Bulletin
    """
    def setUp(self):
        """
        Définition des instances utiles pour l'ensemble de la classe de test.
        """
        commencement = datetime.datetime(2022, 4, 10)
        cloture = datetime.datetime(2022, 4, 25)
        self.presid = Election("Élections présidentielles", (commencement, cloture),
                          ["Macron", "Le Pen", "Mélenchon", "Zemmour", "Péceresse", "Jadot", "Lassalle", "Roussel",
                           "Dupont-Aignan", "Hidalgo", "Poutou", "Arthaud"], [i for i in range(100)], "condorcet")
        self.b1 = Bulletin(self.presid, 1)

    def testInit(self):
        """
        Test d'initialisation du bulletin. Vérifie seulement que les variables d'instance sont bien du type de souhaité.
        """
        self.assertIsInstance(self.b1, Bulletin)
        self.assertIsInstance(self.b1.election, Election)
        self.assertIsInstance(self.b1.id, int)
        self.assertIsInstance(self.b1.valide, bool)
        self.assertIsInstance(self.b1.date, datetime.datetime)

    def testValidite(self):
        """
        Vérifie le fonctionnement du test de validité du bulletin. On montre notamment que si le bulletin compléter
        avant la date d'ouverture ou après la date de cloture du vote, alors la fonction estvalide() retourne False.
        Dans notre cas : - b1 doit être valide - b2 est invalide car le vote survient avant la date d'ouverture - b3
        est invalide car le vote a lieu après la date de cloture - b4 est invalide car l'électeur ne fait pas partie
        de la liste des électeurs.
        """
        b2 = Bulletin(self.presid, 2, t=datetime.datetime(2022, 4, 9))
        b3 = Bulletin(self.presid, 3, t=datetime.datetime(2022, 4, 25, 1))
        b4 = Bulletin(self.presid, 1001)
        test1 = self.b1.estvalide()
        test2 = b2.estvalide()
        test3 = b3.estvalide()
        test4 = b4.estvalide()
        self.assertTrue(test1)
        self.assertFalse(test2)
        self.assertFalse(test3)
        self.assertFalse(test4)

    #########################################################################
    # Ne fonctionne pas car unittest ne gère pas les inputs directement.
    def testComplete(self):
        self.b1.complete()
        self.assertIsInstance(self.b1.bulletin, dict)
        self.assertTrue(self.b1.rempli)
    #########################################################################

class TestListeElectorale(unittest.TestCase):
    """
        Auteur : Jérémy LEMAITRE
        Description : Cette classe teste le bon fonctionnement des méthodes permettant de communiquer avec la
        base de données électeurs.
    """
    entrees = "Sheick Simpore sheick.simpore@ensta-bretagne.org"

    @patch('builtins.input', return_value = entrees)

    def setUp(self):
        """
        Définition des instances utiles pour l'ensemble de la classe de test.
        """

        self.listeElecteurs = ListeElectorale("Présidentielles2022")

    def testInit(self):
        """
            Teste la bonne initialisation de la base de données Electeurs.
            Vérifie seulement que les variables d'instance sont bien du type de souhaité.
        """
        self.assertIsInstance(self.listeElecteurs.name, str)
        self.assertIsInstance(self.listeElecteurs.bdd, sqlite3.Connection)
        self.assertIsInstance(self.listeElecteurs.cursor, sqlite3.Cursor)

    def testInsertion(self, mock_input):
        self.listeElecteurs.ajout_electeur()
        nomelec = self.listeElecteurs.cursor.execute("""SELECT nom FROM Electeurs;""")
        self.assertEqual(nomelec,"Simpore")

if __name__ == '__main__':
    unittest.main()
