def func(filepath):
    import os
    from Bio import SeqIO
    from Bio.SeqUtils import gc_fraction
    numb = 0
    with open(filepath, 'r', encoding='utf-8') as text:
        for text_string in text:
            if text_string.startswith(">"):
                numb += 1
            if numb>10:
                return
        if len(SeqIO.parse(filepath).seq) > 1024:
            return
        else:
            seqs=list(SeqIO.parse(filepath,"fasta"))
            gc = 0
            gcid = 0
            for i in range(len(seqs)):
                gc_new = gc_fraction(seqs[i].seq)
                if gc_new>gc:
                    gc=gc_new
                    gcid=i
    print(f"{seqs[gcid].id}\n{gc*100:.6f}")

os.path.splitext("IN 2.txt")
