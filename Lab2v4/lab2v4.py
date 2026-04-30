import os
from Bio.SeqUtils import molecular_weight

def protein(filepath):
    if not os.path.isabs(filepath):
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath)
    with open(filepath, 'r') as file:
        P = file.readline().strip()
    if len(P)>1000:
        raise ValueError("Длинна >1000")  
    mass=molecular_weight(P, seq_type='protein')
    return mass

protein("IN 1.txt")