from Bio import SeqIO
def cds(gb_path):
    gbs=list(SeqIO.parse(gb_path, "genbank"))
    for gb in gbs:
        for feature in gb.features:
            if feature.type=="CDS":
                sequence=feature.extract(gb.seq)
                protein=sequence.translate()
                at=str(feature.location)
                print(f"{gb.id}: {gb.description}")
                print(f"Coding sequence at = {at}")
                print(f"Translation = {protein}\n")
