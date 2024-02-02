import unittest
<<<<<<< HEAD
from dna.recuit import Recuit  
from dna.RotTable import RotTable
from dna.Traj3D import Traj3D

### BATTERIE DE TEST POUR recuit.py ###

### RUN python -m unittest test_recuit.py ###
### Exemple: en se plaçant dans Genetic-algorithm-for-DNA, entrer: python -m unittest 3dna/test_recuit.py ###



class TestRecuit(unittest.TestCase):

    def setUp(self):
        # Initialisation des objets nécessaires pour les tests
        
        self.rotTable = RotTable()  
        self.recuit = Recuit(self.rotTable, k_max=10, e_min=0.1)

    def test_get_rotTable(self):
        result = self.recuit.get_rotTable()
        self.assertEqual(result, self.rotTable, "La méthode get_rotTable ne renvoie pas la bonne valeur.")

    def test_cost(self):
        dna_seq = "ATCG"
        result = self.recuit.cost(dna_seq, self.rotTable)
        self.assertIsInstance(result, (int, float), "La fonction cost ne renvoie pas un nombre.")

    def test_compute_limits(self):
        self.recuit.compute_limits(self.rotTable)
        result = self.recuit.limits
        self.assertIsInstance(result, dict, "La méthode compute_limits ne remplit pas correctement self.limits.")

    def test_optimization_state(self):
        dna_seq = "ATCG"
        result_table, result_traj = self.recuit.optimization_state(dna_seq)
        self.assertIsInstance(result_table, RotTable, "La méthode optimization_state ne renvoie pas une instance de RotTable.")
        self.assertIsInstance(result_traj, Traj3D, "La méthode optimization_state ne renvoie pas une instance de Traj3D.")

    def test_neighbour(self):
        result = self.recuit.neighbour()
        self.assertIsInstance(result, RotTable, "La méthode neighbour ne renvoie pas une instance de RotTable.")

    def test_probability(self):
        dE = 0.5
        temp = 100
        result = self.recuit.probability(dE, temp)
        self.assertIsInstance(result, float, "La méthode probability ne renvoie pas un nombre décimal.")

    def test_temp(self):
        t = 2.5
        result = self.recuit.temp(t)
        self.assertIsInstance(result, float, "La méthode temp ne renvoie pas un nombre décimal.")

if __name__ == '__main__':
    unittest.main()
=======
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
        self.twist_weight = 300
        self.wedge_weight = 1000

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
        total_cost, distance_cost, alignment_cost, cost_twist_complement, cost_wedge_complement = self.recuit.cost(self.dna_seq, self.rotTable, \
                                                                                                                   self.distance_weight, self.alignment_weight, self.twist_weight, self.wedge_weight)

        self.assertAlmostEqual(total_cost, 37.87999244135347)
        self.assertAlmostEqual(distance_cost, 10.125422644694387)
        self.assertAlmostEqual(alignment_cost,  3.686745017688404)
        self.assertAlmostEqual(cost_twist_complement, 0.0)
        self.assertAlmostEqual(cost_wedge_complement, 0.0)

if __name__ == '_main_':
    unittest.main()
>>>>>>> 9a724ec3ebe76e5c25159e82fef400ba0bf1278b
