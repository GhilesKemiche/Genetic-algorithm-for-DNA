import unittest
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