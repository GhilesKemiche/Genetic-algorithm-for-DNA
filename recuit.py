import random
from 3dna/RotTable.py import RotTable
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class Recuit:
    
    def __init__(self,s,k_max,e_min):
        self.s=s
        self.k_max=k_max
        self.e_min=e_min
        
    @classmethod
    def optimization_state(self,k_max: int,e_min: float, dinucleotide: str, i : int):
        """cherche la table de rotation optimale pour la circularité

        Args:
            k_max (_type_): nb itératio,_
            e_min (_type_): distance petite acceptable
        Retuns:
            s (dict): the optimal Rotation Table         
        """
        s=self.initial_state()
        e=self.cost(s)
        k=0
        
        frame=0
        self.animation(k_max,dinucleotide,2*i)
        self.animation.create(k_max)
        
        
        while k<k_max and e>e_min:
            sn=self.voisin(s)
            en=self.cost(sn)
            self.animation.update(frame,sn,dinucleotide,2*i)
            if en<e or random.random()<self.probability():
                s=sn
                e=en
            k+=1
            frame+=1
        return s
              
        
    @classmethod
    def initial_state(self):
        """Creates an initial Rotation Table

        Returns:
            dict: the Rotation Table
        """
        return RotTable()
    
    
    @classmethod
    def animation(self,k_max,dinucleotide,i):
        def create():
            sns.lineplot(x=[], y=[],)
            plt.xlabel('s')
            plt.ylabel('e (cost)')

        # Fonction de mise à jour pour l'animation
        def update(frame,sn,dinucleotide,i):
            sn_bis=sn.copy()
            en = self.cost(sn_bis)
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
    def cost():
        pass
    
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
        
    @classmethod
    def curbs():
        pass
    
    
        