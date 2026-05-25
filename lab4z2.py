from Bio import SeqIO
def gccount(seq):
    gc = seq.count('G') + seq.count('C')
    total = len(seq)
    return gc / total
def sorting(gbk_file):
    records = []
    for record in SeqIO.parse(gbk_file, "genbank"):
        gc = gccount(record.seq)
        records.append((record, gc))
    records.sort(key=lambda x: x[1])
    for rec, gc in records:
        desc = rec.description
        print(f"{rec.id}: {desc}, GC = {gc}")