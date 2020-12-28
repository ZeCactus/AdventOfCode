rules = {}
myticket = []
nearbytickets = []
with open("input.txt", "r") as file:
    for line in file:
        if line == "\n":
            break
        field = line.split(":")[0]
        ranges = line.split(":")[1].strip()
        arr = []
        for rangez in ranges.split("or"):
            rangez = rangez.strip()
            arr.append((int(rangez.split("-")[0]), int(rangez.split("-")[1])))
        rules[field] = arr
    file.readline()
    for line in file:
        if line == "\n":
            break
        for nr in line.strip().split(","):
            myticket.append(int(nr))
    file.readline()
    for line in file:
        newticket = []
        for nr in line.strip().split(","):
            newticket.append(int(nr))
        nearbytickets.append(newticket)
error = 0
for ticket in nearbytickets:
    for value in ticket:
        flag = False
        for field in rules:
            for valrange in rules[field]:
                if value in range(valrange[0], valrange[1] + 1):
                    flag = True
                    break
        if flag == False:
            error = error + value
print(error)