import unittest
<<<<<<< HEAD
from dna.genetic import *  
from dna.RotTable import RotTable
from dna.Traj3D import Traj3D
from copy import deepcopy

### BATTERIE DE TEST POUR genetic.py ###

### RUN python -m pytest 3dna/test_genetic.py ###
=======
from  dna.genetic import genetic,individu,initialisation
from dna.RotTable import RotTable
from dna.Traj3D import Traj3D
from copy import deepcopy as cp

### BATTERIE DE TEST POUR genetic.py ###

### RUN python -m pytest dna/test_genetic.py ###
### Exemple: en se plaçant dans Genetic-algorithm-for-DNA, entrer: python -m unittest 3dna/test_genetic.py ###
>>>>>>> a5b35a9d35a761f2aee8882a93e0a6a24b48752f

class TestGenetic(unittest.TestCase):

    def setUp(self):
        rot_table=RotTable()
        traj3d=Traj3D()
        folk=individu()
        country=genetic(initialisation(10))
        pass

    def test_initialization(self):
        # Test the initialization of the population
        population_size = 10
        population = initialisation(population_size)
        self.assertEqual(len(population), population_size)

    def test_encoding_chromosomes(self):
        # Test encoding chromosomes for an individual
        ind = individu()
        cop=cp.deepcopy(ind.encode_chromosomes())
        self.assertNotEqual(ind,cop,"aucune modif")
        

    def test_encoding_probas(self):
        # Test encoding probabilities for an individual
        ind = individu()
<<<<<<< HEAD
        if len(decompose_dict_list(ind.chromosome_twist)) != 0:
            cop=cp.deepcopy(ind.encode_probas())
            self.assertNotEqual(ind,cop,"aucune modif")
=======
        cop=cp.deepcopy(ind.encode_probas())
        self.assertNotEqual(ind,cop,"aucune modif")
>>>>>>> a5b35a9d35a761f2aee8882a93e0a6a24b48752f

    def test_mutate(self):
        # Test mutation of an individual
        ind = individu()
<<<<<<< HEAD
        if len(decompose_dict_list(ind.chromosome_twist)) != 0:
            cop=cp.deepcopy(ind.encode_probas())
            ind.mutate()
            self.assertNotEqual(ind,cop,"aucune modif")
=======
        cop=cp.deepcopy(ind.encode_probas())
        ind.mutate()
        self.assertNotEqual(ind,cop,"aucune modif")
>>>>>>> a5b35a9d35a761f2aee8882a93e0a6a24b48752f

    def test_evaluation(self):
        # Test the evaluation function in the genetic class
        dna_seq = "ATCG"
        population = initialisation(10)
        gen_alg = genetic(population)
        evaluation = gen_alg.do_evaluation(dna_seq)
<<<<<<< HEAD
        self.assertIsInstance(evaluation, dict,"erreur de typage")
=======
        self.assertIsInstance(float,"erreur de typage")
>>>>>>> a5b35a9d35a761f2aee8882a93e0a6a24b48752f

    def test_selection(self):
        # Test the selection function in the genetic class
        population = initialisation(10)
        gen_alg = genetic(population)
        gen_alg.do_evaluation("ATCG")
<<<<<<< HEAD
        selection = gen_alg.do_selection(1)
=======
        selection = gen_alg.do_selection()
>>>>>>> a5b35a9d35a761f2aee8882a93e0a6a24b48752f
        self.assertEqual(len(selection),len(population)//2,"la population n'est pas divisée par 2")

    def test_crossover(self):
        # Test the crossover function in the genetic class
        population = initialisation(10)
        gen_alg = genetic(population)
        gen_alg.do_evaluation("ATCG")
<<<<<<< HEAD
        gen_alg.do_selection(1)
        crossover = gen_alg.do_croisement()
        self.assertIsInstance(crossover, list,"non type")
=======
        gen_alg.do_selection()
        crossover = gen_alg.do_croisement()
        self.assertIsInstance(list,"non type")
>>>>>>> a5b35a9d35a761f2aee8882a93e0a6a24b48752f
        
    def test_mutation(self):
        # Test the mutation function in the genetic class
        population = initialisation(10)
        gen_alg = genetic(population)
        gen_alg.do_evaluation("ATCG")
<<<<<<< HEAD
        gen_alg.do_selection(1)
=======
        gen_alg.do_selection()
>>>>>>> a5b35a9d35a761f2aee8882a93e0a6a24b48752f
        gen_alg.do_croisement()
        mutation = gen_alg.do_mutation()
        self.assertEqual(len(mutation),len(population),"nb different d'individus")
        
    def test_algorithm(self):
        # Test the entire genetic algorithm
        dna_seq = "ATCG"
        population = initialisation(10)
        gen_alg = genetic(population)
        gen_alg.algo_gen(5, dna_seq)
        self.assertIsNotNone(gen_alg,"erreur typage")





if __name__ == '__main__':
    unittest.main()