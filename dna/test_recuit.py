import unittest
import numpy as np
from dna.recuit import * 
from dna.RotTable import RotTable

### RUN python -m pytest dna/test_recuit.py ###

class TestRecuit(unittest.TestCase):
    """
    Classe TestRecuit pour tester les différentes méthodes de la classe Recuit.
    """

    def setUp(self):
        """
        Méthode appelée avant chaque test pour configurer l'environnement de test. 
        Initialise une instance de Recuit et RotTable, ainsi que les paramètres de base.
        """
        self.rotTable = RotTable()  
        self.recuit = Recuit(self.rotTable)
        self.dna_seq = "ATCG"  
        self.init_temp = 1
        self.distance_weight = 0.1
        self.alignment_weight = 10.0

    def test_probability(self):
        """
        Teste la méthode probability de la classe Recuit.
        Vérifie que la probabilité calculée est égale à la valeur attendue.
        """
        dE = -1
        temp = 1
        expected_prob = np.exp(-dE / temp)
        result_prob = self.recuit.probability(dE, temp)
        self.assertAlmostEqual(result_prob, expected_prob, msg="La fonction probability ne retourne pas la valeur attendue.")

    def test_temp(self):
        """
        Teste la méthode temp de la classe Recuit.
        Vérifie que la température calculée est égale à la valeur attendue.
        """
        t = 0.5
        t0 = 40
        expected_temp = t0 * (1 - t)
        result_temp = self.recuit.temp(t, t0)
        self.assertEqual(result_temp, expected_temp, msg="La fonction temp ne retourne pas la valeur attendue.")

    def test_cost(self):
        """
        Teste la méthode cost de la classe Recuit.
        Vérifie que le coût total et ses composants (distance, alignement, twist, wedge) sont égaux aux valeurs attendues.
        """
        total_cost, distance_cost, alignment_cost, cost_twist_complement, cost_wedge_complement = self.recuit.cost(self.dna_seq, self.rotTable, self.distance_weight, self.alignment_weight)

        self.assertAlmostEqual(total_cost, 37.87999244135347)
        self.assertAlmostEqual(distance_cost, 10.125422644694387)
        self.assertAlmostEqual(alignment_cost,  3.686745017688404)
        self.assertAlmostEqual(cost_twist_complement, 0.0)
        self.assertAlmostEqual(cost_wedge_complement, 0.0)

if __name__ == '_main_':
    unittest.main()