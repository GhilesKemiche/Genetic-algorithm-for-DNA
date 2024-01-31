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
            self.chromosome_twist[dinucleotide] = resize_bin(dec_to_bin(1000*self.rotTable.getTwist(dinucleotide)),16)
            self.chromosome_wedge[dinucleotide] = resize_bin(dec_to_bin(1000*self.rotTable.getWedge(dinucleotide)),16)

    def encode_probas(self):
        L_t = 1/len(decompose_dict_list(self.chromosome_twist))
        L_w = 1/len(decompose_dict_list(self.chromosome_wedge))
        for dinucleotide in self.rotTable.getTable().keys():
            print(len(self.chromosome_twist[dinucleotide]))
            self.proba_twist[dinucleotide] = list_to_str(np.random.binomial(1,L_t,len(self.chromosome_twist[dinucleotide])))
            self.proba_wedge[dinucleotide] = list_to_str(np.random.binomial(1,L_w,len(self.chromosome_wedge[dinucleotide])))
            
    def mutate(self):
        for dinucleotide in self.rotTable.getTable().keys():
            for i in range(len(list(self.proba_twist[dinucleotide]))):
                if int(list(self.proba_twist[dinucleotide])[int(i)]) == 1:
                    k = abs(int(list(self.chromosome_twist[dinucleotide])[int(i)])-1)
                    self.chromosome_twist[dinucleotide] = change_str(self.chromosome_twist[dinucleotide],i,str(k))
        

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
 

    def f_selection(self):
        popu=cp.deepcopy(self.population)
        fighters=[]
        for folk in popu:
            fighters.append([folk,self.evaluation(folk)])
        best,worst=[None,0],[None,np.inf]
        for i in range(len(fighters)):
            if fighters[i][1]>best[1]:
                best[0]=i
                best[1]=fighters[i][1]
            if fighters[i][1]<=worst[1]:
                worst[0]=i
                worst[1]=fighters[i][1]
            
        arena=[]
        winners=[]
        fighters.pop(worst)
        winners.append(fighters.pop(best))
        while len(fighters):
            if not len(fighters)%2:
                i,j=random.randint(0,len(fighters)-1),random.randint(0,len(fighters)-1)
                while i==j:
                    j=random.randint(0,len(fighters)-1)
                x=fighters.pop(i)
                y=fighters.pop(j)
                arena.append([x,y])
        
        for fight in arena:
            surprise=(abs(fight[0][1]-fight[1][1]))/(abs(fight[0][1]+fight[1][1]))
            if fight[0][1]>fight[1][1]:
                weak,strong=fight[1],fight[0]
            elif fight[0][1]<=fight[1][1]:
                weak,strong=fight[0],fight[1]
            if random.random()<surprise:
                winners.append(weak)
            else:
                winners.append(strong)

        return [winners[i][0] for i in range(len(winners))]
        

    def croisement(self):
        # On construit notre nouvelle population croisement à partir de la population sélectionnée
        N = len(selection)
        for x in selection:
            croisement.append(x)
        
        for x in croisement:
            encode_chromosomes(x)
        
        i = 0
        j = 0
        k = 0
        while(len(croisement) < len(population)):
            # On choisit aléatoirement deux individus parmi les sélectionnés
            i = random.randint(0,N-1)
            j = random.randint(0,N-1)

            # On choisit aléatoirement un point pour le croisement en un point
            k = random.randint(0,16)
            nouvel_individu = individu()
            
            # On effectue le croisement au point k pour chaque gêne des chromosomes twist et wedge
            for dinucleotide in self.rotTable.getTable().keys():
                nouvel_individu.chromosome_twist[dinucleotide] = croisement[i].chromosome_tiwst[dinucleotide][0:k] \
                                                                 + croisement[j].chromosome_twist[dinucleotide][k:-1]
                nouvel_individu.chromosome_wedge[dinucleotide] = croisement[i].chromosome_wedge[dinucleotide][0:k] \
                                                                 + croisement[j].chromosome_wedge[dinucleotide][k:-1]
            croisement.append(nouvel_individu)

        return self.croisement

    def mutation(self):
        for i in self.croisement:
            self.mutation.append(i.mutate())
        return self.mutation
