def rabbits(a):
    if a <= 0:
        return 0
    if a == 1 or a == 2:
        return 1
    prev = 1
    cur = 1
    for i in range(3, a + 1):
        prev = cur
        cur = prev + cur
    return cur