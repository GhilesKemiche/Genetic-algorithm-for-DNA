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




'''Classe individu, relatif aux opérations sur les chromosomes. Chaque individu possède 4 set de chromosomes, un chromosome pour le twist, un pour le wedge et deux
autres pour les probabilités de changementa associés. Chaque chromosome possède des gènes, chaque gène représente le twist/wedge/proba associé à une dinucléotide.'''
class individu:

    #Initialisation   
    def __init__(self):
        self.rotTable = generate_rotTable()
        self.chromosome_twist = {}
        self.chromosome_wedge = {}
        self.proba_twist = {}
        self.proba_wedge = {}
        
    #Méthode qui créé des chromosomes : des dictionnaires dont les clés sont les dinuclétoides, les gènes étant les twist/wedge en binaire
    def encode_chromosomes(self):
        for dinucleotide in self.rotTable.getTable().keys():
            self.chromosome_twist[dinucleotide] = resize_bin(dec_to_bin(1000*self.rotTable.getTwist(dinucleotide)),16)
            self.chromosome_wedge[dinucleotide] = resize_bin(dec_to_bin(1000*self.rotTable.getWedge(dinucleotide)),16)

    #Méthode qui créé des probas : des dictionnaires de meme nature que les chromosomes
    def encode_probas(self):
        L_t = 1/len(decompose_dict_list(self.chromosome_twist))
        L_w = 1/len(decompose_dict_list(self.chromosome_wedge))
        for dinucleotide in self.rotTable.getTable().keys():
            print(len(self.chromosome_twist[dinucleotide]))
            self.proba_twist[dinucleotide] = list_to_str(np.random.binomial(1,L_t,len(self.chromosome_twist[dinucleotide])))
            self.proba_wedge[dinucleotide] = list_to_str(np.random.binomial(1,L_w,len(self.chromosome_wedge[dinucleotide])))
            
    #Méthode de mutation : pour chaque gène des probas, quand on rencontre un 1, on inverse la valeur du caractère correspondant dans le chromosome
    def mutate(self):
        for dinucleotide in self.rotTable.getTable().keys():
            for i in range(len(list(self.proba_twist[dinucleotide]))):
                if int(list(self.proba_twist[dinucleotide])[int(i)]) == 1:
                    k = abs(int(list(self.chromosome_twist[dinucleotide])[int(i)])-1)
                    self.chromosome_twist[dinucleotide] = change_str(self.chromosome_wedge[dinucleotide],i,str(k))
                if int(list(self.proba_wedge[dinucleotide])[int(i)]) == 1:
                    k = abs(int(list(self.chromosome_wedge[dinucleotide])[int(i)])-1)
                    self.chromosome_wedge[dinucleotide] = change_str(self.chromosome_wedge[dinucleotide],i,str(k))
        
    def extract_rotTable(self):
        self.rotTable = merge_dict(back_to_dec(self.chromosome_twist),back_to_dec(self.chromosome_wedge))
        

'''Classe genetic, permettant d'appliquer les étapes de l'algorithme à une liste d'individus'''
class genetic:

    def __init__(self,population):
        self.population = population
        self.evaluation = []
        self.selection = []
        self.croisement = []
        self.mutation = []
        
    


    def do_evaluation(self,dna_seq):
        for x in self.population:
            self.evaluation[x] = self.fitness(x.rotTable, dna_seq)
        self.evalutation = dict(sorted(self.evaluation.items(), key=lambda item: item[1]))
            
        return self.evaluation
 

    def do_selection(self,i):
        fighters=self.evaluation(self)
        best,worst=[None,np.inf],[None,0]
        fighters_l=[]
        iter=0
        for k,v in fighters.items():
            fighters_l.append([k,v])
            if v<best[1]:
                best[0]=iter
                best[1]=v
            if v>=worst[1]:
                worst[0]=iter
                worst[1]=v
            iter+=1
       
        arena=[]
        winners=[]
        fighters_l.pop(worst[0])
        winners.append(fighters_l.pop(best[0]))
        while len(fighters_l):
            if not len(fighters_l)%2:
                i,j=random.randint(0,len(fighters_l)-1),random.randint(0,len(fighters_l)-1)
                while i==j:
                    j=random.randint(0,len(fighters_l)-1)
                x=fighters_l.pop(i)
                y=fighters_l.pop(j)
                arena.append([x,y])
            else:
                return "population odd"
        
        for fight in arena:
            surprise=(abs(fight[0][1]-fight[1][1]))/((i+1)*abs(fight[0][1]+fight[1][1]))
            if fight[0][1]<fight[1][1]:
                weak,strong=fight[1],fight[0]
            elif fight[0][1]>=fight[1][1]:
                weak,strong=fight[0],fight[1]
            if random.random()<surprise:
                winners.append(weak)
            else:
                winners.append(strong)

        self.selection = [winners[i][0] for i in range(len(winners))]
        

    def do_croisement(self):
        # On construit notre nouvelle population croisement à partir de la population sélectionnée
        N = len(self.selection)
        for x in self.selection:
            self.croisement.append(x)
        
        for x in self.croisement:
            self.encode_chromosomes(x)
        
        i = 0
        j = 0
        k = 0
        while(len(self.croisement) < len(self.population)):
            # On choisit aléatoirement deux individus parmi les sélectionnés
            i = random.randint(0,N-1)
            j = random.randint(0,N-1)

            # On choisit aléatoirement un point pour le croisement en un point
            k = random.randint(1,16)
            nouvel_individu = individu()
            
            # On effectue le croisement au point k pour chaque gène des chromosomes twist et wedge
            for dinucleotide in self.rotTable.getTable().keys():
                nouvel_individu.chromosome_twist[dinucleotide] = self.croisement[i].chromosome_twist[dinucleotide][0:k] \
                                                                 + self.croisement[j].chromosome_twist[dinucleotide][k:-1]
                nouvel_individu.chromosome_wedge[dinucleotide] = self.croisement[i].chromosome_wedge[dinucleotide][0:k] \
                                                                 + self.croisement[j].chromosome_wedge[dinucleotide][k:-1]
            self.croisement.append(nouvel_individu)

        return self.croisement

    def do_mutation(self):
        for i in self.croisement:
            i.encode_probas()
            self.mutation.append(i.mutate())
        return self.mutation
    
    
    def fitness(self,rotTable,dna_seq):
        traj3d = Traj3D()
        traj3d.compute(dna_seq, rotTable)
        trajectory = traj3d.getTraj()
        traj_start = np.array(trajectory[0][:-1])
        traj_end = np.array(trajectory[-1][:-1])
        distance_cost = np.linalg.norm(traj_start - traj_end)
        return distance_cost
    
    def initialisation(self,n):
        if n%2:
            return "population odd"
        popu=[]
        for i in range(n):
            folk=individu()
            popu.append(folk)
        return popu

    
    
    def algo_gen(self,n,k,dna_seq):
        popu=self.initialisation(n)
        process=genetic(popu)
        for i in range(k):
            process.evaluation=process.do_evaluation(dna_seq)
            process.selection=process.do_selection(i)
            process.croisement=process.do_croisement()
            process.mutation=process.do_mutation()
            print(len(process.mutation))
            process.population=process.mutation
        return process.population

    
    







        

