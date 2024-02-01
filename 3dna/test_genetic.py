import unittest
from .genetic import *  
from .RotTable import RotTable
from .Traj3D import Traj3D

### BATTERIE DE TEST POUR genetic.py ###

### RUN python -m unittest test_genetic.py ###
### Exemple: en se plaçant dans Genetic-algorithm-for-DNA, entrer: python -m unittest 3dna/test_genetic.py ###

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
        ind.encode_chromosomes()
        # Add more specific assertions based on your requirements

    def test_encoding_probas(self):
        # Test encoding probabilities for an individual
        ind = individu()
        ind.encode_probas()
        # Add more specific assertions based on your requirements

    def test_mutate(self):
        # Test mutation of an individual
        ind = individu()
        ind.encode_probas()
        ind.mutate()
        # Add more specific assertions based on your requirements

    def test_evaluation(self):
        # Test the evaluation function in the genetic class
        dna_seq = "ATCG"
        population = initialisation(10)
        gen_alg = genetic(population)
        evaluation = gen_alg.do_evaluation(dna_seq)
        # Add more specific assertions based on your requirements

    def test_selection(self):
        # Test the selection function in the genetic class
        population = initialisation(10)
        gen_alg = genetic(population)
        gen_alg.do_evaluation("ATCG")
        selection = gen_alg.do_selection()
        # Add more specific assertions based on your requirements

    def test_crossover(self):
        # Test the crossover function in the genetic class
        population = initialisation(10)
        gen_alg = genetic(population)
        gen_alg.do_evaluation("ATCG")
        gen_alg.do_selection()
        crossover = gen_alg.do_croisement()
        # Add more specific assertions based on your requirements

    def test_mutation(self):
        # Test the mutation function in the genetic class
        population = initialisation(10)
        gen_alg = genetic(population)
        gen_alg.do_evaluation("ATCG")
        gen_alg.do_selection()
        gen_alg.do_croisement()
        mutation = gen_alg.do_mutation()
        # Add more specific assertions based on your requirements

    def test_algorithm(self):
        # Test the entire genetic algorithm
        dna_seq = "ATCG"
        population = initialisation(10)
        gen_alg = genetic(population)
        gen_alg.algo_gen(5, dna_seq)
        # Add more specific assertions based on your requirements





if __name__ == '__main__':
    unittest.main()