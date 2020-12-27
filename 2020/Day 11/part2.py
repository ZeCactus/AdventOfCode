import copy
seats = []
with open("input.txt") as file:
    for line in file:
        seats.append(line.strip())
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
while True:
    # for line in seats:
    #     print(line)
    # print()
    flag = False
    newseats = []
    for i in range(0, len(seats)):
        newrow = ""
        for j in range(0, len(seats[i])):
            if seats[i][j] == ".":
                newrow = newrow + "."
                continue
            neighbours = 0

            for direction in directions:
                xmod = direction[0]
                ymod = direction[1]
                x = i
                y = j
                while True:
                    x = x + xmod
                    y = y + ymod
                    if x >= len(seats) or x < 0 or y >= len(seats[0]) or y < 0:
                        break
                    if seats[x][y] == "#":
                        neighbours = neighbours + 1
                        break
                    if seats[x][y] == "L":
                        break





            if seats[i][j] == "L":
                if neighbours == 0:
                    newrow = newrow + "#"
                    flag = True
                else:
                    newrow = newrow + "L"
            if seats[i][j] == "#":
                if neighbours < 5:
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