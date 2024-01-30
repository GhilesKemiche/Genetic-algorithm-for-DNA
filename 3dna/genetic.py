import random
from .RotTable import RotTable
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from .Traj3D import Traj3D
import copy as cp


class genetic:
    
    def __init__(self,rotTable):
        self.rotTable = rotTable
        self.table = rotTable.getTable()
        
    def encodage(self):
        pass
    
    def initialisation(self):
        pass
    
    def evaluation(self):
        pass
    
    def selection(self):
        pass
    
    def croisement(self):
        pass
    
    def mutation(self):
        pass
    
    