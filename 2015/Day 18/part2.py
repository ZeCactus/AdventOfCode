import copy
def lit_neighbours(x, y):
    global lights
    lit = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if x+i < 0 or x+i >= len(lights):
                continue
            if y+j < 0 or y+j >= len(lights[x]):
                continue
            if lights[x+i][y+j] == "#":
                lit += 1
    return lit
inputf = open("input.txt", "r")
lights = [[char for char in line] for line in inputf.read().split()]
lights[0][0] = "#"
lights[0][-1] = "#"
lights[-1][0] = "#"
lights[-1][-1] = "#"
for i in range(0, 100):
    newlights = copy.deepcopy(lights)
    for x in range(0, len(lights)):
        for y in range(0, len(lights[x])):
            if x in [0, len(lights)-1] and y in [0, len(lights[x])-1]:
                newlights[x][y] = "#"
                continue
            if lights[x][y] == "#":
                if lit_neighbours(x, y) in [2, 3]:
                    newlights[x][y] = "#"
                else:
                    newlights[x][y] = "."
            else:
                if lit_neighbours(x, y) == 3:
                    newlights[x][y] = "#"
                else:
                    newlights[x][y] = "."
    lights = copy.deepcopy(newlights)
l = 0
for line in lights:
    l += line.count("#")
print(l)
