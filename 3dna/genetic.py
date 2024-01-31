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
      self.chromosome_twist[dinucleotide] = bin(rotTable.getTwist[dinucleotide])
      self.chromosome_wedge[dinucleotide] = bin(rotTable.getWedge[dinucleotide])

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




def dec_to_bin(number, places=15):
  whole, dec = str(number).split(".")
  whole = int(whole)
  dec = int(dec)
  res = bin(whole).lstrip("0b") + "."
  for x in range(places):
    whole, dec = str((decimal_converter(dec)) * 2).split(".")
    dec = int(dec)
    res += whole
  return float(res)

def decimal_converter(num):
  while(num>1):
    num /= 10
  return num

def bin_to_dec(binary):
  binary = str(binary)
  whole_str, *dec_str = binary.split('.')

  whole_dec = int(whole_str, 2)
  dec_dec = 0.

  if dec_str:
    for k in range(len(dec_str[0])):
      if(dec_str[0][k] == '1'):
        dec_dec = dec_dec + float(2**(-k-1))
  else:
    dec_dec = 0

  return whole_dec + dec_dec


# Call the function as : quicksort(A,0,len(A)-1)
def quicksort(A, lo, hi):
  if lo >= hi or lo < 0:
    return

  p = partition(A, lo, hi)

  quicksort(A, lo, p - 1)
  quicksort(A, p + 1, hi)

def partition(A, lo, hi):
  pivot = A[hi]
  i = lo - 1

  for j in range(lo,hi):
    if A[j]<=pivot:
      i = i + 1
      A[i], A[j] = A[j], A[i]

  i = i + 1
  A[i], A[hi] = A[hi], A[i]
  return i
