def adjust(corner1, corner2, value):
    for i in range(corner1[0], corner2[0]+1):
        for j in range(corner1[1], corner2[1]+1):
            lights[i][j] += value
            if lights[i][j] < 0:
                lights[i][j] = 0

inputf = open("input.txt", "r")
outputf = open("test.txt", "w")
lights = [[0]*1000 for i in range(0, 1000)]
for line in inputf.read().split("\n"):
    instructions = line.split()
    corner1 = instructions[1].split(',')
    corner1 = [int(x) for x in corner1]
    corner2 = instructions[3].split(',')
    corner2 = [int(x) for x in corner2]
    if instructions[0] == "toggle":
        value = 2
    if instructions[0] == "on":
        value = 1
    if instructions[0] == "off":
        value = -1
    adjust(corner1, corner2, value)
brightness = 0
for line in lights:
    for light in line:
        brightness += light
        outputf.write(str(light) + "\n")
        
outputf.close()
print(brightness)
