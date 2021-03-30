import copy
seats = []
with open("input.txt") as file:
    for line in file:
        seats.append(line.strip())
while True:
    flag = False
    newseats = []
    for i in range(0, len(seats)):
        newrow = ""
        for j in range(0, len(seats[i])):
            if seats[i][j] == ".":
                newrow = newrow + "."
                continue
            neighbours = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if x == i and y == j:
                        continue
                    try:
                        if x == -1 or y == -1:
                            continue
                        if seats[x][y] == "#":
                            neighbours = neighbours + 1
                    except IndexError:
                        continue
            if seats[i][j] == "L":
                if neighbours == 0:
                    newrow = newrow + "#"
                    flag = True
                else:
                    newrow = newrow + "L"
            if seats[i][j] == "#":
                if neighbours < 4:
                    newrow = newrow + "#"
                else:
                    newrow = newrow + "L"
                    flag = True
        newseats.append(copy.deepcopy(newrow))
    seats = copy.deepcopy(newseats)
    if flag == False:
        break
occ = 0
for line in seats:
    occ = occ + line.count("#")
print(occ)