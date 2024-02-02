import unittest
from dna.genetic import *  
from dna.RotTable import RotTable
from dna.Traj3D import Traj3D
from copy import deepcopy

### BATTERIE DE TEST POUR genetic.py ###

### RUN python -m pytest 3dna/test_genetic.py ###

class TestGenetic(unittest.TestCase):

    def setUp(self):
       
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
        if len(decompose_dict_list(ind.chromosome_twist)) != 0:
            cop=cp.deepcopy(ind.encode_probas())
            self.assertNotEqual(ind,cop,"aucune modif")

    def test_mutate(self):
        # Test mutation of an individual
        ind = individu()
        if len(decompose_dict_list(ind.chromosome_twist)) != 0:
            cop=cp.deepcopy(ind.encode_probas())
            ind.mutate()
            self.assertNotEqual(ind,cop,"aucune modif")

    def test_evaluation(self):
        # Test the evaluation function in the genetic class
        dna_seq = "ATCG"
        population = initialisation(10)
        gen_alg = genetic(population)
        evaluation = gen_alg.do_evaluation(dna_seq)
        self.assertIsInstance(evaluation, dict,"erreur de typage")

    def test_selection(self):
        # Test the selection function in the genetic class
        population = initialisation(10)
        gen_alg = genetic(population)
        gen_alg.do_evaluation("ATCG")
        selection = gen_alg.do_selection(1)
        self.assertEqual(len(selection),len(population)//2,"la population n'est pas divisée par 2")

    def test_crossover(self):
        # Test the crossover function in the genetic class
        population = initialisation(10)
        gen_alg = genetic(population)
        gen_alg.do_evaluation("ATCG")
        gen_alg.do_selection(1)
        crossover = gen_alg.do_croisement()
        self.assertIsInstance(crossover, list,"non type")
        
    def test_mutation(self):
        # Test the mutation function in the genetic class
        population = initialisation(10)
        gen_alg = genetic(population)
        gen_alg.do_evaluation("ATCG")
        gen_alg.do_selection(1)
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
