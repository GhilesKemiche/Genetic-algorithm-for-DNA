from .RotTable import RotTable
from .Traj3D import Traj3D
from .recuit import Recuit

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
    
    

    

    
    
    k_max=1000
    e_min=1
    recuit=Recuit(rot_table,k_max,e_min)
    rot_table_opt, traj = recuit.optimization_state( seq)
    traj.compute(seq, rot_table_opt)
    # print(traj.getTraj())
    traj.draw()
    traj.write(args.filename+".png")
    print(rot_table_opt)


if __name__ == "__main__" :
    main()
