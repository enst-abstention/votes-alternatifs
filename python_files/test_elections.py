from elections import *
from scrutins import *
import unittest
import datetime


class TestElection(unittest.TestCase):
    def setUp(self):
        ouverture = datetime.datetime(2022,4,10)
        cloture = datetime.datetime(2022,4,25)
        self.presid = Election("Élections présidentielles",(ouverture, cloture), ["Macron", "Le Pen", "Mélenchon", "Zemmour", "Péceresse", "Jadot", "Lassalle", "Roussel", "Dupont-Aignan", "Hidalgo", "Poutou", "Arthaud"], [i for i in range(100)], "condorcet")
        self.presid2 = Election("Élections présidentielles", (cloture, ouverture), ["Macron", "Le Pen", "Mélenchon", "Zemmour", "Péceresse", "Jadot", "Lassalle", "Roussel", "Dupont-Aignan", "Hidalgo", "Poutou", "Arthaud"], [i for i in range(100)],"jugement majoritaire")

    def testInit(self):
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
        valide = self.presid.verif_elec(48)
        invalide = self.presid.verif_elec(1004)
        self.assertEqual(invalide, False)
        self.assertEqual(valide, True)


class TestBulletin(unittest.TestCase):
    def setUp(self):
        commencement = datetime.datetime(2022, 4, 10)
        cloture = datetime.datetime(2022, 4, 25)
        presid = Election("Élections présidentielles", (commencement, cloture), ["Macron", "Le Pen", "Mélenchon", "Zemmour", "Péceresse", "Jadot", "Lassalle", "Roussel", "Dupont-Aignan", "Hidalgo", "Poutou", "Arthaud"], [i for i in range(100)], "condorcet")
        self.b1 = Bulletin(presid)

    def testInit(self):
        self.assertIsInstance(self.b1, Bulletin)
        self.assertIsInstance(self.b1.election, Election)
        self.assertIsInstance(self.b1.id, int)
        self.assertIsInstance(self.b1.valide, bool)
        self.assertIsInstance(self.b1.date, datetime.datetime)

    def testValidite(self):
        return



if __name__ == '__main__':
    unittest.main()
