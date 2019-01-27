def sortByHeight(a):
    people = sorted(x for x in a if x >= 0)
    res = []
    for x in a:
        res.append(x if x < 0 else people.pop(0))
    return res

print(sortByHeight([-1,7,5,6,-1,-1,4]))
