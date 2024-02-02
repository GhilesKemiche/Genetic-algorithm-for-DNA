import random
from .RotTable import RotTable
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
from .Traj3D import Traj3D
import copy as cp

class Recuit:
    
    def __init__(self, rotTable):
        """Initialise l'algorithme de recuit simulé avec une table de rotation donnée.
        
        Args:
            rotTable: Une instance de la classe RotTable contenant la table de rotation initiale.
        """
        self.rotTable = rotTable
        self.traj3d = Traj3D()
        self.limits = {}
        
    def get_rotTable(self):
        """Retourne la table de rotation actuelle."""
        return self.rotTable
    
    def cost(self, dna_seq, rot_table, distance_weight, alignment_weight, twist_weight, wedge_weight):
        """Calcule le coût d'une séquence d'ADN donnée avec une table de rotation.
        
        Le coût est calculé en se basant sur la distance entre le début et la fin de la trajectoire 3D,
        ainsi que l'alignement des directions au début et à la fin de la trajectoire.
        
        Args:
            dna_seq (str): La séquence d'ADN.
            rot_table : La table de rotation 
            distance_weight : le poids de la distance dans la minimisation
            alignment_weight : le poids de l'alignement dans la minimisation
        Returns:
           Le coût total, le coût de distance et le coût d'alignement.
        """

        #calculer la trajectoire de la table donnée
        traj3d = self.traj3d
        traj3d.compute(dna_seq, rot_table)
        trajectory = traj3d.getTraj()

        #calculer la distance entre le dernier et le premier point de la trajectoire
        traj_start = np.array(trajectory[0][:-1])
        traj_end = np.array(trajectory[-1][:-1])
        distance_cost = np.linalg.norm(traj_start - traj_end)

        #calculer la direction du dernier et premier vecteur direction
        direction_start = np.array(trajectory[1][:-1]) - traj_start  
        direction_end = traj_end - np.array(trajectory[-2][:-1])
        direction_start = direction_start / np.linalg.norm(direction_start)
        direction_end = direction_end / np.linalg.norm(direction_end)
        cos_angle = np.dot(direction_start, direction_end)
        cos_angle = np.clip(cos_angle, -1, 1)
        angle = np.arccos(cos_angle)
        alignment_cost = np.degrees(angle) 

        #Calculer la somme des differences des twists et wedge des 
        list_complement = [('AA', 'TT'), ('AC', 'GT'), ('AG', 'CT'), ('CA', 'TG'), ('CC', 'GG'), ('GA', 'TC')]
        list_differences_twist = [np.abs(rot_table.getTwist(case[0])- rot_table.getTwist(case[1])) for case in list_complement]
        list_differences_wedge = [np.abs(rot_table.getWedge(case[0])- rot_table.getWedge(case[1])) for case in list_complement]
        cost_twist_complement = sum(list_differences_twist)
        cost_wedge_complement = sum(list_differences_wedge)

        #Calculer le cout total
        total_cost = distance_weight * distance_cost + alignment_cost * alignment_weight + twist_weight* cost_twist_complement + wedge_weight* cost_wedge_complement
        return total_cost, distance_cost, alignment_cost, cost_twist_complement, cost_wedge_complement

    def compute_limits(self, rotTable):
        """Calcule et stocke les limites des valeurs de rotation pour chaque dinucléotide dans le dictionnaire limits.
        
        Args:
            rotTable : La table de rotation 
        """
        dict = {}
        table = rotTable.rot_table
        
        for di in table:
            dict[di] = [np.array([table[di][0] - table[di][3], table[di][0] + table[di][3]]),
                        np.array([table[di][1] - table[di][4], table[di][1] + table[di][4]])]
        self.limits = dict
    
    def optimization_state(self, dna_seq: str, max_iter: int, cost_min, init_temp: float = 1,\
                            distance_weight  = 1.0, alignment_weight = 100.0, \
                                twist_weight = 300, wedge_weight = 1000):
        """Exécute l'optimisation par recuit simulé pour trouver la table de rotation optimale.
        
        L'algorithme continue jusqu'à atteindre le nombre maximum d'itérations ou un coût minimum.
        
        Args:
            dna_seq (str): La séquence d'ADN à optimiser.
            max_iter (int): Le nombre maximum d'itérations.
            cost_min (float): Le coût minimum acceptable.
            init_temp (float): La température initiale pour le recuit simulé.
            distance_weight : le poids à accorder à la distance pendant  l'optimisation
            alignment_weight : le poids à accorder à l'alignement pendant l'optimisation
        Returns:
           La table de rotation optimale et la trajectoire 3D correspondante.
        """
        cost, distance_cost, alignment_cost, cost_twist_complement, cost_wedge_complement = self.cost(dna_seq, self.get_rotTable(), distance_weight,\
                                                                                                       alignment_weight, twist_weight, wedge_weight)
        k = 0
        
        while k < max_iter and cost > cost_min:
            neighbour = self.neighbour()
            cost_neighbour, distance_cost, alignment_cost, cost_twist_complement, cost_wedge_complement  = \
                self.cost(dna_seq, neighbour, distance_weight, alignment_weight, twist_weight, wedge_weight)
            
            if cost_neighbour < cost or random.random() < self.probability(cost_neighbour - cost, self.temp(k / max_iter, t0 = init_temp)):
                print(f'cost = {cost_neighbour}   distance = {distance_cost}    theta = {alignment_cost}    k = {k}    twist = {cost_twist_complement}  wedge = {cost_wedge_complement}')
                self.rotTable = neighbour
                cost = cost_neighbour
            k += 1
        self.traj3d.compute(dna_seq, self.rotTable)
        
        return self.rotTable, self.traj3d
    
    def neighbour(self):
        """Génère une table de rotation voisine en modifiant légèrement la rotation pour deux dinucléotides choisis aléatoirement.
        
        Les nouvelles valeurs sont choisies dans les limites permises pour chaque dinucléotide.
        
        Returns:
            La nouvelle table de rotation voisine.
        """
        Rot_copy = cp.deepcopy(self.rotTable) 
        table = Rot_copy.rot_table
        
        self.compute_limits(Rot_copy)
        table_limit = self.limits
        choose_keys = np.random.choice(list(table.keys()), 2)
        for dinucleotide in choose_keys:
            twist, wedge = Rot_copy.getTwist(dinucleotide), Rot_copy.getWedge(dinucleotide)
            t_inf, t_sup = table_limit[dinucleotide][0] - twist
            w_inf, w_sup = table_limit[dinucleotide][1] - wedge
            
            Rot_copy.setTwist(dinucleotide, twist + np.random.uniform(t_inf, t_sup) / 100)
            Rot_copy.setWedge(dinucleotide, wedge + np.random.uniform(w_inf, w_sup) / 100)
        
        return Rot_copy
    
    def probability(self, dE, temp):
        """Calcule la probabilité d'accepter un état voisin avec un coût plus élevé.
        
        La probabilité est calculée en utilisant la distribution de Boltzmann.
        
        Args:
            dE : La différence de coût entre l'état actuel et l'état voisin.
            temp : La température actuelle dans le processus de recuit.
            
        Returns:
            La probabilité d'accepter l'état voisin.
        """
        return np.exp(-dE / temp)
    
    def temp(self, t, t0=40):
        """Calcule la température pour une itération donnée en utilisant un schéma de refroidissement.
        
        Args:
            t : Le ratio de l'itération actuelle par rapport au nombre total d'itérations.
            t0 : La température initiale.
            
        Returns:
            La température pour l'itération donnée.
        """
        return t0 * (1 - t)
