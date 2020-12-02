import geom_analysis as ga

def test_calculate_distance():
    coord1 = [0,0,0]
    coord2 = [1,0,0]
    expected = 1.0
    observed = ga.calculate_distance(coord1,coord2)
    assert observed==expected

def test_bond_check():
    atom_dist_one=2.0
    atom_dist_two=0
    atom_dist_three=0.5
    atom_dist_four=1.5
    expected = False,False,True,True
    observed=ga.bond_check(atom_dist_one),ga.bond_check(atom_dist_two),ga.bond_check(atom_dist_three),ga.bond_check(atom_dist_four)
    assert observed==expected

import pytest

def test_bond_check_neg():
    dist=-1
    expected = False
    with pytest.raises(ValueError):
        observed=ga.bond_check(dist)

def test_open_xyz_error():
    fname='hello.txt'
    with pytest.raises(ValueError):
        ga.open_xyz(fname)
