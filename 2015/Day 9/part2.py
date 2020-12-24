import itertools
inputf = open("input.txt", "r")
locations = inputf.read().split("\n")
inputf.close()
names = []
for line in locations:
    line = line.split()
    if line[0] not in names:
        names.append(line[0])
    if line[2] not in names:
        names.append(line[2])
distances = [[0] * len(names) for i in range(0, len(names))]
for line in locations:
    line = line.split()
    x1 = names.index(line[0])
    x2 = names.index(line[2])
    distances[x1][x2] = int(line[4])
    distances[x2][x1] = int(line[4])
permute = []
for i in range(0, len(names)):
    permute.append(i)
permutations = list(itertools.permutations(permute))
max_distance = float("-inf")
for permutation in permutations:
    distance = 0
    for i in range(0, len(permutation)-1):
        distance += distances[permutation[i]][permutation[i+1]]
    if distance > max_distance:
        max_distance = distance
print(max_distance)
