from scrutins import Scrutin,Condorcet,JugementMajoritaire
import unittest


class TestScrutin(unittest.TestCase):
    """"
    Test creation Scrutin
    """

    def setUp(self):
        self.bull =[{'Melencon': 1, 'Macron': 2, 'Pecresse': 3,'Le_Pen':4,'Zemour':5},
                    {'Melencon': 2, 'Macron': 1, 'Pecresse': 4,'Le_Pen':3,'Zemour':5}]
        self.s = Scrutin(['Melenchon', 'Macron', 'Le_Pen','Zemour','Pecresse'])

    def test_egalite_liste_candidat(self):
        self.assertEqual(self.s.candidats,['Melenchon', 'Macron', 'Le_Pen','Zemour','Pecresse'])

    def test_egalite_liste_bulletins(self):
        self.assertEqual(self.bull,[{'Melencon': 1, 'Macron': 2, 'Pecresse': 3,'Le_Pen':4,'Zemour':5},
                                    {'Melencon': 2, 'Macron': 1, 'Pecresse': 4,'Le_Pen':3,'Zemour':5}])

    def test_taille_de_chaque_bulletin_de_vote(self):
        for i in self.bull :
            for j in self.bull :
                self.assertEqual(len(i),len(j))

    def test_chaque_candidat_a_au_moins_ete_classe(self):
        for i in self.bull :
            self.assertEqual(len(i),len(self.s.candidats))

    def test_scrutins_is_instance_of_scrutin(self):
        self.assertIsInstance(self.s,Scrutin)


class TestCondorcet(unittest.TestCase):
    """
    Test creation mode de scrutin de Condorcet
    """

    def setUp(self):
        self.bull = [{'Melencon': 1, 'Macron': 2, 'Pecresse': 3,'Le_Pen':4,'Zemour':5},
                     {'Melencon': 2, 'Macron': 1, 'Pecresse': 4,'Le_Pen':3,'Zemour':5}]
        self.c =Condorcet(['Melenchon', 'Macron', 'Le_Pen','Zemour','Pecresse'])

    def test_egalite_liste_candidat(self):
        self.assertEqual(self.c.candidats,['Melenchon', 'Macron', 'Le_Pen','Zemour','Pecresse'])


class TestJugementMajoritaire(unittest.TestCase):

    """"
    Test creation mode de scrutin JugementMajoritaire
    """

    def setUp(self):
        self.bull = [{'Melencon': 1, 'Macron': 2, 'Pecresse': 3, 'Le_Pen': 4, 'Zemour': 5},
                     {'Melencon': 2, 'Macron': 1, 'Pecresse': 4, 'Le_Pen': 3, 'Zemour': 5}]
        self.b = JugementMajoritaire(['Melenchon', 'Macron', 'Le_Pen', 'Zemour', 'Pecresse'])

    def test_egalite_liste_candidat(self):
        self.assertEqual(self.b.candidats, ['Melenchon', 'Macron', 'Le_Pen', 'Zemour', 'Pecresse'])




if __name__ == '__main__':
    unittest.main()