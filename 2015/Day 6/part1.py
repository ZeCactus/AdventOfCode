def toggle(corner1, corner2):
    for i in range(corner1[0], corner2[0]+1):
        for j in range(corner1[1], corner2[1]+1):
            lights[i][j] *= -1

inputf = open("input.txt", "r")
lights = [[-1]*1000 for i in range(0, 1000)]
for line in inputf.read().split("\n"):
    instructions = line.split()
    corner1 = instructions[1].split(',')
    corner1 = [int(x) for x in corner1]
    corner2 = instructions[3].split(',')
    corner2 = [int(x) for x in corner2]
    if instructions[0] == "toggle":
        toggle(corner1, corner2)
        continue
    light = -1 if instructions[0] == "off" else 1
    for i in range(corner1[0], corner2[0]+1):
        for j in range(corner1[1], corner2[1]+1):
            lights[i][j] = light
on = 0
for line in lights:
    on += line.count(1)
