from .RotTable import RotTable
from .Traj3D import Traj3D
from .recuit import Recuit
import numpy as np
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename of DNA sequence")
parser.parse_args()
args = parser.parse_args()

def main():
    start_time = time.time()

    
    rot_table = RotTable()
    
    # Read file
    lineList = [line.rstrip('\n') for line in open(args.filename)]
    # Formatting
    seq = ''.join(lineList[1:])


    n=100
    k=50
    algo=genetic(initialisation(n))
    algo.algo_gen(k,seq)
    
    # if len(seq) > 10000 :
    #     distance_weight = 0.12
    #     alignment_weight = 10
    #     init_temp = 50.0
    #     max_iter = 10000 
    #     cost_min = 50
    #     twist_weight = 30
    #     wedge_weight = 100
    # else : 
    #     distance_weight = 1.2
    #     alignment_weight = 50
    #     init_temp = 1.0
    #     max_iter = 15000 
    #     cost_min = 50
    #     twist_weight = 300
    #     wedge_weight = 1000
    
    # np.random.seed(seed = 750)
    # recuit=Recuit(rot_table)
    # rot_table_opt, traj = recuit.optimization_state(seq, max_iter= max_iter, cost_min= cost_min,\
    #                                                  init_temp= init_temp, distance_weight= distance_weight,\
    #                                                       alignment_weight= alignment_weight, twist_weight = twist_weight, wedge_weight = wedge_weight)
    # traj.compute(seq, rot_table_opt)
    # # print(traj.getTraj())
    # print('la table de rotation optimale est : \n', rot_table_opt.getTable())
    # traj.draw()
    # traj.write(args.filename+".png")





    end_time = time.time()
    print()
    print(f"Temps d'exécution : {end_time - start_time} secondes")



if __name__ == "__main__" :
    main()
