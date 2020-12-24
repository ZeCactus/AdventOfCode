from itertools import permutations as perms
inputf = open("input.txt", "r")
text = inputf.read()
inputf.close()
values = text.split("\n")
values = [values[i].split() for i in range(0, len(values))]
people = []
for item in values:
    if item[0] not in people:
        people.append(item[0])
people.append("Me")
d = {person:{human:0 for human in people if human != person} for person in people}
for value in values:
    d[value[0]][value[2]] = int(value[1])
max_happiness = float("-inf")
permutations = list(perms(people))
for p in permutations:
    happiness = 0
    p = list(p)
    for i in range(0, len(p)-1):
        happiness += d[p[i]][p[i-1]]
        happiness += d[p[i]][p[i+1]]
    happiness += d[p[-1]][p[-2]]
    happiness += d[p[-1]][p[0]]
    if happiness > max_happiness:
        max_happiness = happiness
print(max_happiness)
