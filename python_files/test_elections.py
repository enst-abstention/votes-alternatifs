from elections import *
from scrutins import *
import unittest


class TestElection(unittest.TestCase):
    def setUp(self) :
        self.presid = Election("Élections présidentielles",("2022-04-10","2022-04-24"), ["Macron", "Le Pen", "Mélenchon", "Zemmour", "Péceresse", "Jadot", "Lassalle", "Roussel", "Dupont-Aignan", "Hidalgo", "Poutou", "Arthaud"], [i for i in range(100)], "condorcet")

    def testInit(self):
        self.assertIsInstance(self.presid.scrutin, Condorcet)


class TestBulletin(unittest.TestCase):
    def setUp(self) :
        presid = Election("Élections présidentielles", ("2022-04-10", "2022-04-24"),
                               ["Macron", "Le Pen", "Mélenchon", "Zemmour", "Péceresse", "Jadot", "Lassalle", "Roussel",
                                "Dupont-Aignan", "Hidalgo", "Poutou", "Arthaud"], [i for i in range(100)], "condorcet")
        self.b1 = Bulletin(presid)

    def testInit(self):
        self.assertIsInstance(self.b1, Bulletin)


if __name__ == '__main__':
    unittest.main()
