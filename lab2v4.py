from Bio.SeqUtils import molecular_weight

def protein(filepath):
    with open(filepath, 'r') as file:
        P = file.readline().strip()
    if len(P)>1000:
        raise ValueError("Длинна >1000")  
    mass=molecular_weight(P, seq_type='protein')
    return mass

protein("C:\\Users\\user\\Downloads\\IN 1.txt")