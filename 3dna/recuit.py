import random
from .RotTable import RotTable
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from .Traj3D import Traj3D


class Recuit:
    
    def __init__(self,rot_table,k_max,e_min):
        self.rot_table=rot_table
        self.traj3d=Traj3D()
        self.k_max=k_max
        self.e_min=e_min
        
    @classmethod
    def optimization_state(self,k_max: int,e_min: float, dinucleotide: str, i : int, dna_seq: str):
        """cherche la table de rotation optimale pour la circularité

        Args:
            k_max (_type_): nb itératio,_
            e_min (_type_): distance petite acceptable
        Retuns:
            s (dict): the optimal Rotation Table         
        """
        self.rot_table=self.initial_state()
        e=self.cost(dna_seq,self.rot_table)
        k=0
        temp=25
        lamb = 0.99
        
        frame=0
        self.animation(k_max,dinucleotide,2*i)
        self.animation.create(k_max)
        
        
        while k<k_max and e>e_min:
            sn=self.voisin()
            en=self.cost(dna_seq)
            temp = lamb * temp
            self.animation.update(frame,sn,dinucleotide,2*i)
            if en<e or random.random()<self.probability(en-e,temp):
                self.rot_table=sn
                e=en
            k+=1
            frame+=1
        return self.rot_table
              
        
    @classmethod
    def initial_state(self):
        """Creates an initial Rotation Table

        Returns:
            dict: the Rotation Table
        """
        return RotTable()
    
    
    @classmethod
    def animation(self,k_max,dinucleotide,i,dna_seq):
        def create():
            sns.lineplot(x=[], y=[],)
            plt.xlabel('s')
            plt.ylabel('e (cost)')

        # Fonction de mise à jour pour l'animation
        def update(frame,sn,dinucleotide,i,dna_seq):
            sn_bis=sn.copy()
            en = self.cost(dna_seq)
            sn_aim=sn_bis[dinucleotide][2*i]
            x=np.linspace(s_min, s_max,100)
            l_sn=[]
            for i in range(len(x)):
                sn_bis[dinucleotide][2*i]=x[i]
                l_sn.append(sn_bis.copy())
            y=[self.cost(val) for val in l_sn]
            sns.lineplot(x,y, label='Coût en fonction de la table pour un angle donné')
    
            # Ajouter le point (sn, en) à la courbe
            plt.scatter(sn_aim, en, c='red', s=100)
            
            plt.title(f'Itération {frame + 1}')
            
        # Initialisation des variables
        s_min = self.initial_state()[dinucleotide][2*i]- self.initial_state()[dinucleotide][2*i+1] # Valeur minimale de s
        s_max = self.initial_state()[dinucleotide][2*i]+ self.initial_state()[dinucleotide][2*i+1]  # Valeur maximale de s

        # Création de l'animation
        animation = FuncAnimation(plt.gcf(), update, frames=self.k_max, init_func=create, blit=False, repeat=False)

        # Affichage de l'animation
        plt.show()
        
        
    @classmethod
    def cost(self, dna_seq, rot_table):
        traj3d = Traj3D()
        traj3d.compute(dna_seq, rot_table)
        traj_start = traj3d.getTraj()[0]
        traj_end = traj3d.getTraj()[-1]
        cost = np.linalg.norm(traj_start - traj_end)
        
        return cost

    
    #Méthode qui calcule les intervalles
    def compute_limits(self, RotTable):
        dict = {}
        table = RotTable.rot_table
        
        for di in table:
            dict[di] = [np.array([table[di][0]-table[di][3],table[di][0]+table[di][3]]),
                        np.array([table[di][1]-table[di][4],table[di][1]+table[di][4]])]
        return dict
    
    
    #Méthode qui calcule les voisins   
    def neighbour(self, RotTable):
        table = RotTable.rot_table
        table_limit = RotTable.compute_limits()
        for dinucleotide in table.keys():
            twist, wedge = RotTable.getTwist(dinucleotide), RotTable.getWedge(dinucleotide)
            t_inf, t_sup = table_limit[dinucleotide][0] - twist 
            w_inf, w_sup = table_limit[dinucleotide][1] - wedge
            
            RotTable.setTwist(dinucleotide,twist+np.random.uniform(t_inf,t_sup))
            RotTable.setWedge(dinucleotide,wedge+np.random.uniform(w_inf,w_sup))
    
    def probability(dE,temp):
        return np.exp(-dE/temp)
    
    def temp():
