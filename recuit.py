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
        
    @classmethod
    def neighbor():
        
    @classmethod
    def probability():
        
    @classmethod
    def curbs()
    
    @classmethod
    def 
        
    
        