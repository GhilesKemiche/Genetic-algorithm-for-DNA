import random
from .RotTable import RotTable
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
from .Traj3D import Traj3D
import copy as cp

class Recuit:
    
    def __init__(self,rotTable,k_max,e_min):
        self.rotTable=rotTable
        self.traj3d=Traj3D()
        self.k_max=k_max
        self.e_min=e_min
        self.limits = {}
        
    def get_rotTable(self):
        return self.rotTable
        

    
              
    

    # def animation(self,dinucleotide,i):
    #     def create():
    #         sns.lineplot(x=[], y=[],)
    #         plt.xlabel('s')
    #         plt.ylabel('e (cost)')

    #     # Fonction de mise à jour pour l'animation
    #     def update(frame,sn,dinucleotide,i,dna_seq):
    #         sn_bis=cp.deepcopy(sn)
    #         en = self.cost(dna_seq,sn_bis)
    #         sn_aim=sn_bis[dinucleotide][2*i]
    #         x=np.linspace(s_min, s_max,100)
    #         l_sn=[]
    #         for i in range(len(x)):
    #             sn_bis[dinucleotide][2*i]=x[i]
    #             l_sn.append(cp.deepcopy(sn_bis))
    #         y=[self.cost(dna_seq,val) for val in l_sn]
    #         sns.lineplot(x,y, label='Coût en fonction de la table pour un angle donné')
    
    #         # Ajouter le point (sn, en) à la courbe
    #         plt.scatter(sn_aim, en, c='red', s=100)
            
    #         plt.title(f'Itération {frame + 1}')
            
    #     # Initialisation des variables
    #     a = RotTable()
    #     initial_state = a.rot_table
    #     s_min = initial_state[dinucleotide][2*i]- initial_state[dinucleotide][2*i+1] # Valeur minimale de s
    #     s_max = initial_state[dinucleotide][2*i]+ initial_state[dinucleotide][2*i+1]  # Valeur maximale de s

    #     # Création de l'animation
    #     animation = FuncAnimation(plt.gcf(), update, frames=self.k_max, init_func=create, blit=False, repeat=False)

    #     # Affichage de l'animation
    #     plt.show()
        
        
    
    def cost(self, dna_seq, rot_table):
        traj3d = self.traj3d
        traj3d.compute(dna_seq, rot_table)
        traj_start = traj3d.getTraj()[0]
        traj_end = traj3d.getTraj()[-1]
        cost = np.linalg.norm(traj_start - traj_end)
    
        
        return cost

    
    #Méthode qui calcule les intervalles
    def compute_limits(self,rotTable):
        dict = {}
        table = rotTable.rot_table
        
        for di in table:
            dict[di] =  [np.array([table[di][0]-table[di][3],table[di][0]+table[di][3]]),
                        np.array([table[di][1]-table[di][4],table[di][1]+table[di][4]])]
        self.limits = dict
    
    def optimization_state(self, dna_seq: str):
        """cherche la table de rotation optimale pour la circularité

        Args:
            k_max (type): nb itératio,_
            e_min (type): distance petite acceptable
        Retuns:
            s (dict): the optimal Rotation Table         
        """
        
        e=self.cost(dna_seq,self.get_rotTable())
        k=0
        lamb = 0.95
        

        
        # self.animation(self.k_max,dinucleotide,2*i)
        # self.animation.create(self.k_max)
        
        
        while k<self.k_max and e>self.e_min:
            sn=self.neighbour()
            en=self.cost(dna_seq,sn)
            print(en)
            
            #self.animation.update(frame,sn,dinucleotide,2*i)
            if en<e or random.random()<self.probability(en-e,self.temp(k/(self.k_max))):
                
                self.rotTable=sn
                
                e=en
            k+=1
        self.traj3d.compute(dna_seq, self.rotTable)
        
        return self.rotTable, self.traj3d
    
    #Méthode qui calcule les voisins   
    def neighbour(self):
        
        Rot_copy = cp.deepcopy(self.rotTable) 
        table = Rot_copy.rot_table
        
        
        self.compute_limits(Rot_copy)
        table_limit = self.limits
        choose_keys = np.random.choice(list(table.keys()),2)
        for dinucleotide in choose_keys:
            twist, wedge = Rot_copy.getTwist(dinucleotide), Rot_copy.getWedge(dinucleotide)
            t_inf, t_sup = table_limit[dinucleotide][0] - twist
            w_inf, w_sup = table_limit[dinucleotide][1] - wedge
            
            Rot_copy.setTwist(dinucleotide,twist+np.random.uniform(t_inf,t_sup)/10)
            Rot_copy.setWedge(dinucleotide,wedge+np.random.uniform(w_inf,w_sup)/10)


        return Rot_copy
    
    def probability(self, dE,temp):
        if not temp:
            return 1
        
        return np.exp(-dE/temp)
    
    def temp(self,t,t0=10):
        return t0*(1-t)
        
    