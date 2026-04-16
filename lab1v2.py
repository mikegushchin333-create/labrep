def calculate_rabbits(n, m):
    rabbits = [0] * (n + 1)
    rabbits[1] = 1
    if n >= 2:
        rabbits[2] = 1
    for i in range(3, n + 1):
        newborns = rabbits[i - 2]
        rabbits[i] = rabbits[i - 1] + newborns
        if i > m:
            rabbits[i] -= rabbits[i - m - 1]
    return rabbits[n]