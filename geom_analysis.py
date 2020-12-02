"""
This module has functions associated with analyzing the geometry of a molecule.

When run as a script and given an xyz file, this script will print out the bonds. Run

$ python geometry_analysis.py --help

to see input options.
"""

import numpy
import os
import argparse

def calculate_distance(atom1_coord, atom2_coord):
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    bond_length_12 = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return bond_length_12

def bond_check(atom_distance, minimum_length=0, maximum_length=1.5):
    if atom_distance<0:
        raise ValueError(F'Invalid atom distance {atom_distance}. Distance cannot be less than 0!')
    if atom_distance > minimum_length and atom_distance <= maximum_length:
        return True
    else:
        return False

def open_xyz(filename):
    if '.xyz' not in filename:
        raise ValueError(F' Invalid file {filename}. File type must be xyz')
    else:
        xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
        symbols = xyz_file[:,0]
        coord = (xyz_file[:,1:])
        coord = coord.astype(numpy.float)
        return symbols, coord

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='This script analyzes a user given xyz file and outputs the length of the bonds.')
    parser.add_argument('xyz_file',help='The filepath for the xyz file to analyze')
    args=parser.parse_args()
    xyzfilename=args.xyz_file

    parser.add_argument('-minimum_length', help='The minimum distance to consider atoms bonded.', type=float, default=0)
    parser.add_argument('-maximum_length', help='The maximum distance to consider atoms bonded.', type=float, default=1.5)
    symbols, coord = open_xyz(xyzfilename)
    num_atoms = len(symbols)
    for num1 in range(0,num_atoms):
         for num2 in range(0,num_atoms):
             if num1<num2:
                 bond_length_12 = calculate_distance(coord[num1], coord[num2])
                 if bond_check(bond_length_12,minimum_length=args.minimum_length,maximum_length=args.maximum_length) is True:
                     print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')
