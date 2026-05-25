from Bio import SeqIO
from Bio.Seq import translate
import os
def func(filepath):
    if not os.path.isabs(filepath):
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath)
    for record in SeqIO.parse(filepath, "genbank"):
        for feature in record.features:
            if feature.type == "CDS":
                location = feature.location
                cds_seq = location.extract(record.seq)
                protein = translate(cds_seq, table=1, to_stop=False)
                strand = "+" if location.strand == 1 else "-"
                start = location.start
                end = location.end
                loc_str = f"[{start}:{end}] ({strand})"
                print(f"{record.id}: {record.description}")
                print(f"Coding sequence location = {loc_str}")
                print(f"Translation = {protein}\n")
                
                
func("columba.gb")