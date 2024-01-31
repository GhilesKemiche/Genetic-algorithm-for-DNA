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
    
        
        
    def cost(self, dna_seq, rot_table):
            traj3d = self.traj3d
            traj3d.compute(dna_seq, rot_table)
            trajectory = traj3d.getTraj()
            traj_start = np.array(trajectory[0][:-1])
            traj_end = np.array(trajectory[-1][:-1])
            distance_cost = np.linalg.norm(traj_start - traj_end)
            direction_start = np.array(trajectory[1][:-1]) - traj_start  
            direction_end = traj_end - np.array(trajectory[-2][:-1]  )
            direction_start = direction_start / np.linalg.norm(direction_start)
            direction_end = direction_end / np.linalg.norm(direction_end)
            cos_angle = np.dot(direction_start, direction_end)
            cos_angle = np.clip(cos_angle, -1, 1)
            angle = np.arccos(cos_angle)
            alignment_cost = np.degrees(angle) 
            distance_weight = 1.0
            alignment_weight = 1.0
            total_cost = distance_weight * distance_cost + alignment_weight * alignment_cost
            
            return total_cost

    
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
        
        
        while k<self.k_max and e>self.e_min:
            sn=self.neighbour()
            en=self.cost(dna_seq,sn)

            if en<e or random.random()<self.probability(en-e,self.temp(k/(self.k_max))):
                print(en)
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
            if random.random()<0.5 : 
                Rot_copy.setTwist(dinucleotide,twist+np.random.uniform(t_inf,t_sup)/10)
            else :
                Rot_copy.setWedge(dinucleotide,wedge+np.random.uniform(w_inf,w_sup)/10)


        return Rot_copy
    
    def probability(self, dE,temp):
        
        return np.exp(-dE/temp)
    
    def temp(self,t,t0=20):
        return t0*(1-t)