inputf = open("input.txt", "r")
total = 0
for line in inputf.read().split():
    dims = [int(nr) for nr in line.split('x')]
    volume = 1
    for n in dims:
        volume*=n
    total += volume
    ltotal = min(dims) * 2
    dims.remove(ltotal/2)
    ltotal += min(dims) * 2
    total += ltotal
print(total)
