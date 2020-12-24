def indexes(string, substring):
    ind = []
    for i in range(0, len(string)-len(substring)+1):
        if string[i:i+len(substring)] == substring:
            ind.append(i)
    return ind
        

inputf = open("input.txt", "r")
inp = inputf.read().split("\n")
molecule = inp[-1]
inp = inp[:-2]
trans = {line.split()[0]:[] for line in inp}
for line in inp:
    trans[line.split()[0]].append(line.split()[2])

transformations = []
amount = 0
for key in trans:
    for value in trans[key]:
        for i in indexes(molecule, key):
            new = molecule[:i] + value + molecule[i+len(key):]
            if new not in transformations:
                transformations.append(new)
                amount += 1
print(amount)
