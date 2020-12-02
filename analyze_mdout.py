import os
import argparse
import glob
import numpy
import matplotlib.pyplot as plt

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='This script parses amber mdout files to extract the total energy.',)
    parser.add_argument('path', help='The filepath to the file to be analyzed.')
    parser.add_argument('plot',default='False',type=bool,choices=[True,False], help='If specified as True a plot of energy will be produced, default = False')
    args=parser.parse_args()
    Amber_filename = args.path
    want_plot=args.plot

    amberfile_list=glob.glob(Amber_filename)

    for item in amberfile_list:
        with open(item) as file:
            amberfile = file.readlines()

        filename=os.path.basename(item)
        filename=filename.split('.')
        filename=filename[0]

        energy_list=[]

        for line in amberfile:
            if 'Etot' in line:
                energy_line=line
                words = energy_line.split()
                energy=words[2]
                energy_list.append(energy)


        Amberdatafile=open(F'{filename}_Etot.txt','w+')

        for energy in energy_list[:-2]:
            Amberdatafile.write(F'{energy} \n')

        Amberdatafile.close()

        if want_plot==True:
            plt.figure()
            plt.plot(energy_list[:-2])
            plt.savefig(F'{filename}.png')
            # if I want to add customization to these plots we can later.
            #but now I have an exam to take
