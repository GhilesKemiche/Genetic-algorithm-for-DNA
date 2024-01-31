import random
from .RotTable import RotTable
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from .Traj3D import Traj3D
import copy as cp



def generate_rotTable():
  random_rotTable = RotTable()

  pass


'''Classe individu, relatif aux opérations sur les chromosomes. Chaque individu possède 4 set de chromosomes, un chromosome pour le twist, un pour le wedge et deux
autres pour les probabilités de changementa associés. Chaque chromosome possède des gènes, chaque gène représente le twist/wedge/proba associé à une dinucléotide.'''
class individu:

  def __init__(self, rotTable, name):
    self.rotTable = rotTable
    self.name = name
    self.chromosome_twist = {}
    self.chromosome_wedge = {}
    self.proba_twist = {}
    self.proba_wedge = {}

  def encode_chromosomes(self):
    for dinucleotide in rotTable.getTable().keys():
      self.chromosome_twist[dinucleotide] = dec_to_bin(rotTable.getTwist[dinucleotide])
      self.chromosome_wedge[dinucleotide] = dec_to_bin(rotTable.getWedge[dinucleotide])

  def mutate(self):
    L = len(chromosome)
    for dinucleotide in rotTable.getTable().keys():
      self.proba_twist[dinucleotide] = np.random.bernouilli(1/L,len(chromosome))
      self.proba_wedge[dinucleotide] = np.random.bernouilli(1/L,len(chromosome))



    pass


'''Classe genetic, permettant d'appliquer les étapes de l'algorithme à une liste d'individus'''
class genetic:

  def __init_(self,population,fitness):
    self.population = population
    self.fitness = fitness
    self.evaluation = []
    self.selection = []
    self.croisement = []
    self.mutation = []


  def evaluation(self):

    return self.evaluation
    pass

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

