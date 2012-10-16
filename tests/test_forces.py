'''Calculate forces between atoms'''
from chemlab import Atom, Molecule, display
from chemlab.forces import lennard_jones

def test_1():
    a = Atom(1, "Ne", [-1.0, 0.0, 0.0])
    b = Atom(2, "Ne", [1.0, 0.0, 0.0])
    
    am = Molecule([a, b])
    
    
    # Force vector exterted on the first atom
    f = lennard_jones(a, b)


