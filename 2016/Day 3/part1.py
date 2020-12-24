inputf = open("input.txt", "r")
triangles = [[int(value) for value in line.split()] for line in inputf.read().split("\n")]
inputf.close()
actualtriangles = []
for i in range(0, len(triangles), 3):
    tr1 = []
    tr2 = []
    tr3 = []
    tr1.append(triangles[i][0])
    tr1.append(triangles[i+1][0])
    tr1.append(triangles[i+2][0])
    tr2.append(triangles[i][1])
    tr2.append(triangles[i+1][1])
    tr2.append(triangles[i+2][1])
    tr3.append(triangles[i][2])
    tr3.append(triangles[i+1][2])
    tr3.append(triangles[i+2][2])
    actualtriangles.append(tr1)
    actualtriangles.append(tr2)
    actualtriangles.append(tr3)
triangles = actualtriangles
valids = 0
for triangle in triangles:
    if triangle[0] + triangle[1] > triangle[2]:
        if triangle[0] + triangle[2] > triangle[1]:
            if triangle[1] + triangle[2] > triangle[0]:
                valids += 1
print(valids)
