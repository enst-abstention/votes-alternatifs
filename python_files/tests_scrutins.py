from scrutins import Scrutin
import unittest

class TestScrutin(unittest.TestCase):

    def setUp(self):
        self.s = Scrutin(['Jean', 'Yves', 'Jacques'],[{'Jean': 1, 'Yves': 2, 'Jacques': 3}, {'Jean': 2, 'Yves': 1,'Jacques': 3}])

    def test_scrutins_is_instance_of_scrutin(self):
        self.assertIsInstance(self.s,Scrutin)

    def test_scrutin_limite_is_inferieur_n(self):
         self.assertGreater(self.s.limite,2)


    def testcondorcet(self):
        pass


    def testjugementmajoritaire(self):
        pass


if __name__ == '__main__':
    unittest.main()