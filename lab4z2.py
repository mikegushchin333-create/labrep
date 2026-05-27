from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
def gcsort(gb_path):
    gbs = list(SeqIO.parse(gb_path, "genbank"))
    unsorted=[]
    for gb in gbs:
        gc = gc_fraction(gb.seq)
        unsorted.append((gb.id, gb.description, gc))
    sorted_data=sorted(unsorted,key=lambda x: x[2])
    for gb in sorted_data:
            print(f"{gb[0]}: {gb[1]}, GC = {gb[2]}")
