import random
from .RotTable import RotTable
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from .Traj3D import Traj3D
import copy as cp
from .utilitaires import*
from tqdm import tqdm

def generate_rotTable():
    
    rotTable = RotTable()
    
    dict = {}
    table = rotTable.rot_table
        
    for di in table:
        dict[di] =  [np.array([table[di][0]-table[di][3],table[di][0]+table[di][3]]),
                    np.array([table[di][1]-table[di][4],table[di][1]+table[di][4]])]
        
    Rot_copy = cp.deepcopy(rotTable)
        
    table_limit = dict
    choose_keys = np.random.choice(list(table.keys()),5)
    for dinucleotide in choose_keys:
        t_inf, t_sup = table_limit[dinucleotide][0]
        w_inf, w_sup = table_limit[dinucleotide][1]
        Rot_copy.setTwist(dinucleotide,round((random.choice(np.linspace(t_inf,t_sup,100))),2))
        Rot_copy.setWedge(dinucleotide,round((random.choice(np.linspace(w_inf,w_sup,100))),2))

    return Rot_copy




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
            self.chromosome_twist[dinucleotide] = resize_bin(dec_to_bin(int(1000*self.rotTable.getTwist(dinucleotide))),16)
            self.chromosome_wedge[dinucleotide] = resize_bin(dec_to_bin(int(1000*self.rotTable.getWedge(dinucleotide))),16)

    #Méthode qui créé des probas : des dictionnaires de meme nature que les chromosomes
    def encode_probas(self):
        L_t = 1/len(decompose_dict_list(self.chromosome_twist))
        L_w = 1/len(decompose_dict_list(self.chromosome_wedge))
        for dinucleotide in self.rotTable.getTable().keys():
            self.proba_twist[dinucleotide] = list_to_str(np.random.binomial(1,0.008,len(self.chromosome_twist[dinucleotide])))
            self.proba_wedge[dinucleotide] = list_to_str(np.random.binomial(1,0.008,len(self.chromosome_wedge[dinucleotide])))
            
    #Méthode de mutation : pour chaque gène des probas, quand on rencontre un 1, on inverse la valeur du caractère correspondant dans le chromosome
    def mutate(self):
        for dinucleotide in self.rotTable.getTable().keys():
            for i in range(len(list(self.proba_twist[dinucleotide]))):
                if int(list(self.proba_twist[dinucleotide])[int(i)]) == 1:
                    k = abs(int(list(self.chromosome_twist[dinucleotide].replace('b','0'))[int(i)])-1)
                    self.chromosome_twist[dinucleotide] = change_str(self.chromosome_wedge[dinucleotide],i,str(k))
                if int(list(self.proba_wedge[dinucleotide])[int(i)]) == 1:
                    k = abs(int(list(self.chromosome_wedge[dinucleotide].replace('b','0'))[int(i)])-1)
                    self.chromosome_wedge[dinucleotide] = change_str(self.chromosome_wedge[dinucleotide],i,str(k))
        
        
    def extract_rotTable(self,extract=False):
        for key in self.rotTable.getTable().keys():
            self.rotTable.setTwist(key,back_to_dec(self.chromosome_twist)[key])
            self.rotTable.setWedge(key,back_to_dec(self.chromosome_wedge)[key])
        if extract==True:
            return self.rotTable

'''Classe genetic, permettant d'appliquer les étapes de l'algorithme à une liste d'individus'''
class genetic:

    def __init__(self,population):
        self.population = population
        self.evaluation = {}
        self.selection = []
        self.croisement = []
        self.mutation = []


    def do_evaluation(self,dna_seq):
        self.evaluation={}
        for x in self.population:
            self.evaluation[x] = self.fitness(x.rotTable, dna_seq)
        self.evaluation = ordonner_dictionnaire_par_valeur(self.evaluation)
        return self.evaluation
 

    def do_selection(self,u):
        fighters=cp.deepcopy(self.evaluation)
        compte=0
        for k,v in fighters.items():
            
            if not compte:
                best,worst= [0,v],[0,v]
            compte+=1
        fighters_l=[]
        iter=0
        
        for k,v in fighters.items():
            fighters_l.append([k,v])
            if v<best[1]:
                best[0]=iter
                best[1]=v
            elif v>=worst[1]:
                worst[0]=iter
                worst[1]=v
            iter+=1
       
        arena=[]
        winners=[]
        
        
        fighters_l.pop(worst[0])
        print(best[1])
        if best[0]>=worst[0]:
            best[0]-=1
        winners.append(fighters_l.pop(best[0]))
        
        while len(fighters_l):
            if not len(fighters_l)%2:
                
                i,j=random.randint(0,len(fighters_l)-1),random.randint(0,len(fighters_l)-1)
                
                while i==j:
                    j=random.randint(0,len(fighters_l)-1)
                    
                x=fighters_l.pop(i)
                
                if j >= len(fighters_l):
                    j = len(fighters_l) - 1
        
                y=fighters_l.pop(j)
                arena.append([x,y])
            else:
                return "population odd"
        
        for fight in arena:
            surprise=min(10*(abs(fight[0][1]-fight[1][1]))/((u+1)*abs(fight[0][1]+fight[1][1])),0.2)
            
            if fight[0][1]<fight[1][1]:
                weak,strong=fight[1],fight[0]
            elif fight[0][1]>=fight[1][1]:
                weak,strong=fight[0],fight[1]
            if random.random()<surprise:
                winners.append(weak)
            else:
                winners.append(strong)
        
        self.selection = list(self.evaluation.keys())[0:5]
        
        return self.selection 
        

    def do_croisement(self):
        self.croisement=[]
        # On construit notre nouvelle population croisement à partir de la population sélectionnée
        N = len(self.selection)
        for x in self.selection:
            self.croisement.append(x)
        
        for x in self.croisement:
            x.encode_chromosomes()
        
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
            for dinucleotide in nouvel_individu.rotTable.getTable().keys():
                nouvel_individu.chromosome_twist[dinucleotide] = self.croisement[i].chromosome_twist[dinucleotide][0:k] \
                                                                 + self.croisement[j].chromosome_twist[dinucleotide][k:-1]
                nouvel_individu.chromosome_wedge[dinucleotide] = self.croisement[i].chromosome_wedge[dinucleotide][0:k] \
                                                                 + self.croisement[j].chromosome_wedge[dinucleotide][k:-1]
            self.croisement.append(nouvel_individu)

        return self.croisement
    
    def do_mutation(self):
        self.mutation = []
        for i in self.croisement:
            i.encode_probas()
            i.mutate()
            i.extract_rotTable()
            self.mutation.append(i)
    
        return self.mutation
    
    
    def fitness(self,rotTable,dna_seq):
        traj3d = Traj3D(False)
        traj3d.compute(dna_seq, rotTable)
        trajectory = traj3d.getTraj()
        traj_start = np.array(trajectory[0][:-1])
        traj_end = np.array(trajectory[-1][:-1])
        distance_cost = np.linalg.norm(traj_start - traj_end)
        return distance_cost
    
    

    
    
    def algo_gen(self,k,dna_seq):
        
        for u in tqdm(range(k)):
            self.evaluation=self.do_evaluation(dna_seq)
            self.selection=self.do_selection(u)
            self.croisement=self.do_croisement()
            self.population=self.do_mutation()
            cpt = 0
            for i in self.population:
                if  cpt>0:
                    break
                print(self.fitness(i.rotTable,dna_seq))
                cpt +=1
                
        self.evaluation=self.do_evaluation(dna_seq)
        print(self.evaluation)
        print(type(self.evaluation))
        best=list(self.evaluation.keys())[0]
        print(self.evaluation[best])
        print(self.fitness(best.extract_rotTable(True),dna_seq))
        traj3d=Traj3D(True)
        rot_table=best.extract_rotTable(extract=True)
        traj3d.compute(dna_seq,rot_table)
        traj3d.draw()
    


"python -m 3dna ./data/plasmid_8k.fasta"

def initialisation(n):
        if n%2:
            return "population odd"
        popu=[]
        for i in range(n):
            folk=individu()
            popu.append(folk)
        return popu
    
    







        


