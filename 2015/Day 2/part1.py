inputf = open("input.txt", "r")
total = 0
for line in inputf.read().split():
    dims = [int(nr) for nr in line.split('x')]
    smallest = float("inf")
    ltotal = 0
    dim = dims[0] * dims[1]
    ltotal += dim
    smallest = min(smallest, dim)
    dim = dims[0] * dims[2]
    ltotal += dim
    smallest = min(smallest, dim)
    dim = dims[1] * dims[2]
    ltotal += dim
    ltotal *= 2
    smallest = min(smallest, dim)
    total += smallest
    total += ltotal
print(total)
