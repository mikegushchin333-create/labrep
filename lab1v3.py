def hamming(s,t):
    if len(s) != len(t):
        print("строки разной длины")
    s_letters=list(s)
    t_letters=list(t)
    dH=0
    for i in range(len(s_letters)):
        if s_letters[i] != t_letters[i]:
            dH += 1
    print(dH)
    
hamming("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")


