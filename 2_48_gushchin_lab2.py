
# %%
# Создайте класс SmartHouse (умный дом), отразив при этом основные принципы ООП.
# Поясните логику своего кода.

class SmartHouse:
    def __init__(self, garage):
        self.garage = garage
        self.num_of_ppl = 0
    def comehome(self):
        self.num_of_ppl += 4
        return "семья дома"
    
# house - объект, которому мы присвоили класс SmartHouse, comehome - метод (функция 
# внутри класса)
# %%
# Какой из принципов ООП Вы считаете наиболее полезным?

# Наследование. Код засчёт этого значительно чище.
# %%
# Имеется нижепредставленная последовательность. Напишите функцию, которая 
# удаляет лишние символы, убирает пробелы, приводит к верхнему регистру и разбивает
# строку на триплеты. Результатом функции должна быть строка.

raw_seq =  '''        1 ctgactcaaa cgtctcactg atcgttacac aacaccagtg taatttcgca gtgcttatta
       61 acaagctaaa gcgctagcat ttactggaag cacgacttcc tctcgccaac gtggatataa
      121 agctgtatta atcatgggtg ttcacgactt gtggtccatc gtggagccag tccgagaggc
      181 ggtgccgttg tacagtttga gcggaaagac tctggcggta gacctgagct tatgggtctg
      241 tgaggctcag cAcgtccagg ccatgatggg cagagttatg aagccacatc tgaggaattt
      301 atttttccga gtatcatcgc tcacactgat GGGGtgaag ctcgtctttg tcatggaggg
      361 agaagctccc caacttaaat cagaaacaat gagcaaaagg acagaaatga gattcggagg
      421 atccagaaaa gCCcatttct caaagtcatc cacaactacc agcagagggc gctttaaagc
      481 tgtacttcga gGGGtgtgcag atatgttgaa ctacctgggt gtgccctggg tgacagcagc
      541 tggggaagca gaggccatgt gtgcttacct ggactcagca gggctggttg atggctgcat
      601 caccaacgat ggagatgcat tcttatatgg ggctaggacg gtctacagga acttcaatat
      661 gaacagtaaa gaccctcagg tcgattgcta ccagacatcc cgagtgcaga ccgagctaca
      721 cctgtcaaga gagaatcttg ttggcttggc cattctcctc ggttgtgatt aagcagatgt
      781 gttgtataaa gtaat'''

def fun21(seq):
    seq = seq.strip().lower()
    seq1 = []
    for nucleotide in seq:
        if nucleotide in "agct":
            seq1.append(nucleotide)
    global clean_seq 
    clean_seq = "".join(seq1)
    trip = [clean_seq[i:i+3] for i in range(0, len(clean_seq), 3)]
    global triplets
    triplets = " ".join(trip)
    
# %% 
# Для полученной последовательности вычислите её молекулярную массу, температуру
# плавления, GC-состав, а также длину цепи

def fun22(seq):
    molmass = {"a": 313.21,"g": 329.21,"t": 304.2,"c": 289.18}
    const = 61.69
    weight = 0
    for nucleotide in seq:
        weight += molmass[nucleotide]
    weight = weight - const
    GC_content = (seq.count("g")+seq.count("c"))/len(seq)
    melt_temp = 64.9 +41*(seq.count("g")+seq.count("c")-16.4)/(len(seq))
    print(round(weight,2), "молекулярная масса"), "/n", print(GC_content, "GC-состав"), "/n", print(melt_temp, "темрература плавления"), "/n", print(len(seq), "длина последовательности")

# %%
# через Biopython

# %%
# Из полученной нуклеотидной последовательности из 2.1 сделайте матричную-РНК

def fun23(seq):
    translation_table = str.maketrans("t", "u")
    mrna = seq.translate(translation_table)
    global matrixrna
    matrixrna = mrna

# %%
# через Biopython

# %%
# Через Biopython реализуйте функцию, которая принимает строку с матричной РНК 
# (из прошлого задания 2.3) и преобразует её в список аминокислот, соответствующих
# каждому триплету. При этом функция должна начинать считывание с первого встреченного
# старт-кодона и завершать работу при обнаружении стоп-кодона

from Bio.Data import CodonTable

def fun24(argseq):
    table = CodonTable.unambiguous_dna_by_id[1]
    mrna = argseq.upper().replace(" ", "")
    starts = []
    for codon in table.start_codons:
        position = mrna.find(codon)
        if position != -1:
            starts.append((position,codon))
    start, start_codon = min(starts, key=lambda x: x[0])
    aminolist = []
    for i in range(start, len(mrna)-2,3):
        codon = mrna[i:i+3]
        if codon in table.stop_codons:
            break
        aminolist.append(table.forward_table[codon])
    return aminolist