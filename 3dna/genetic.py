import random
from .RotTable import RotTable
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from .Traj3D import Traj3D
import copy as cp
from .utilitaires import*


def generate_rotTable():
    random_rotTable = RotTable()

    return random_rotTable

def fitness(x):
    return x


'''Classe individu, relatif aux opérations sur les chromosomes. Chaque individu possède 4 set de chromosomes, un chromosome pour le twist, un pour le wedge et deux
autres pour les probabilités de changementa associés. Chaque chromosome possède des gènes, chaque gène représente le twist/wedge/proba associé à une dinucléotide.'''
class individu:

  def __init__(self, name):
    self.rotTable = generate_rotTable()
    self.name = name
    self.chromosome_twist = {}
    self.chromosome_wedge = {}
    self.proba_twist = {}
    self.proba_wedge = {}

  def encode_chromosomes(self):
    for dinucleotide in self.rotTable.getTable().keys():
      self.chromosome_twist[dinucleotide] = dec_to_bin(self.rotTable.getTwist[dinucleotide])
      self.chromosome_wedge[dinucleotide] = dec_to_bin(self.rotTable.getWedge[dinucleotide])

  def encode_probas(self):
    L = len(decompose_dict_list(self.chromosome))
    for dinucleotide in self.rotTable.getTable().keys():
      self.proba_twist[dinucleotide] = list_to_int(np.random.bernouilli(1/L,len(self.chromosome)))
      self.proba_wedge[dinucleotide] = list_to_int(np.random.bernouilli(1/L,len(self.chromosome)))


a = individu("1")
a.encode_chromosomes()
a.encode_probas()
print("Test")
print(a.chromosome_twist)
print(a.proba_twist)

'''Classe genetic, permettant d'appliquer les étapes de l'algorithme à une liste d'individus'''
class genetic:

  def __init__(self,population,fitness):
    self.population = population
    self.fitness = fitness
    self.evaluation = []
    self.selection = []
    self.croisement = []
    self.mutation = []


  def evaluation(self):
    self.evaluation = quicksort(self.fitness(self.population))
    return self.evaluation
 

  def selection(self):

    return self.selection
    pass

  def croisement(self):

    return self.croisement
    pass

  def mutation(self):
    for i in self.croisement:
      self.mutation.append(i.mutate())
    return self.mutation

