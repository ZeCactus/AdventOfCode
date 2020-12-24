import copy
def getnumbers(curr, total, ammount, result, sumto):
    current = copy.copy(curr)
    if ammount == len(current):
        if sum(current) == sumto:
            result.append(current)
        return
    else:
        for i in range(0, total):
            current.append(i)
            getnumbers(current, total-i, ammount, result, sumto)
            current.pop()
    return
