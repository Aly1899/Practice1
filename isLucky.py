def isLucky(n):
    d = map(int, str(n))
    m = len(list(d))
    return sum(d[:m])==sum(d[m:])

isLucky(55)