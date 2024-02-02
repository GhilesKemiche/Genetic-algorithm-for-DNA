from .RotTable import RotTable
from .Traj3D import Traj3D
from .recuit import Recuit
import numpy as np
from .genetic import *


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename of DNA sequence")
parser.parse_args()
args = parser.parse_args()

def main():

    rot_table = RotTable()
    
    # Read file
    lineList = [line.rstrip('\n') for line in open(args.filename)]
    # Formatting
    seq = ''.join(lineList[1:])
    
    
    n=100
    k=50
    
    algo=genetic(initialisation(n))
    algo.algo_gen(k,seq)
    
    
    

    
    

    

    
    """
    seq = ''.join(lineList[1:])
    distance_weight = 1.0
    alignment_weight = 50
    init_temp = 1.0
    max_iter = 14000 
    cost_min = 5
    np.random.seed(seed = 750)
    recuit=Recuit(rot_table)
    rot_table_opt, traj = recuit.optimization_state(seq, max_iter= max_iter, cost_min= cost_min, init_temp= init_temp, distance_weight= distance_weight, alignment_weight= alignment_weight)
    traj.compute(seq, rot_table_opt)
    """
    
    #print(traj.getTraj())
    #traj.draw()
    #traj.write(args.filename+".png")
    #print(rot_table_opt)
    

if __name__ == "__main__" :
    main()