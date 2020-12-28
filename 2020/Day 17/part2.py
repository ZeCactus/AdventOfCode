import operator
import copy
import time
def display(actives):
    min_x = float("inf")
    max_x = float("-inf")
    min_y = float("inf")
    max_y = float("-inf")
    for active in actives:
        x = active[0]
        y = active[1]
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    grid = []
    for i in range(1 + max_x - min_x):
        row = []
        for j in range(1+max_y-min_y):
            row.append(".")
        grid.append(row)
    centerx = len(grid)//2
    centery = len(grid[0])//2
    for active in actives:
        grid[active[0] - min_x][active[1] - min_y] = "#"
    for line in grid:
        print(line)
    print()
start = time.time()
actives = []
with open("input.txt","r") as file:
    z = 0
    w = 0
    x = 0
    for line in file:
        y = 0
        for char in line.strip():
            if char == "#":
                actives.append((x,y,z,w))
            y = y + 1
        x = x + 1
dirs = []
for i in range(-1, 2):
    for j in range(-1, 2):
        # if i != 0 or j != 0:
        #     dirs.append((i,j, 0))
        for k in range(-1, 2):
            for w in range(-1, 2):
                if i != 0 or j != 0 or k != 0 or w != 0:
                    dirs.append((i,j,k,w))

for i in range(0, 6):
    tocheck = []
    for active in actives:
        for dir in dirs:
            neighbor = tuple(map(operator.add, active, dir))
            if neighbor not in tocheck:
                tocheck.append(neighbor)
    newactives = []
    for cube in tocheck:
        neighbors = 0
        for dir in dirs:
            if tuple(map(operator.add, cube, dir)) in actives:
                neighbors = neighbors + 1
        if cube in actives:
            if neighbors == 2 or neighbors == 3:
                if cube not in newactives:
                    newactives.append(cube)
        else:
            if neighbors == 3:
                if cube not in newactives:
                    newactives.append(cube)
    actives = copy.copy(newactives)
print(len(actives))
print(int(time.time() - start))