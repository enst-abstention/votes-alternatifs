from scrutins import Scrutin
import unittest

class TestScrutin(unittest.TestCase):

    def setUp(self):
        self.bull =
        self.s = Scrutin(['Melenchon', 'Macron', 'Le_Pen','Zemour','Pecresse'],[{'Melencon': 1, 'Macron': 2, 'Pecresse': 3,'Le_Pen':4,'Zemour':5}, {'Melencon': 2, 'Macron': 1, 'Pecresse': 4,'Le_Pen':3,'Zemour':5}])

    def test_egalite_liste_candidat(self):
        self.assertEqual(self.s.candidats,['Melenchon', 'Macron', 'Le_Pen','Zemour','Pecresse'])

    def test_egalite_liste_bulletins(self):
        self.assertEqual(self.s.bulletins,[{'Melencon': 1, 'Macron': 2, 'Pecresse': 3,'Le_Pen':4,'Zemour':5}, {'Melencon': 2, 'Macron': 1, 'Pecresse': 4,'Le_Pen':3,'Zemour':5}])

    def test_taille_de_chaque_bulletin_de_vote(self):
        for i in self.s.bulletins :
            for j in self.s.bulletins :
                self.assertEqual(len(i),len(j))

    def test_chaque_candidat_a_au_moins_ete_classe(self):
        for i in self.s.bulletins :
            self.assertEqual(len(i),len(self.s.candidats))

    def test_scrutins_is_instance_of_scrutin(self):
        self.assertIsInstance(self.s,Scrutin)

    def test_scrutin_limite_is_inferieur_n(self):
         self.assertGreater(self.s.limite,2)




if __name__ == '__main__':
    unittest.main()