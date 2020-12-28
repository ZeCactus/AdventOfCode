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
valids = []
for ticket in nearbytickets:
    flag = True
    for value in ticket:
        inflag = False
        for field in rules:
            for valrange in rules[field]:
                if value in range(valrange[0], valrange[1] + 1):
                    inflag = True
        if inflag == False:
            flag = False
    if flag == True:
        valids.append(ticket)
poss = {}
for i in range(0, len(rules)):
    poss[i] = [key for key in rules]
for i in range(0, len(valids[0])):
    for ticket in valids:
        for field in poss[i]:
            inflag = False
            for valrange in rules[field]:
                if ticket[i] in range(valrange[0], valrange[1] + 1):
                    inflag = True
            if inflag == False:
                poss[i].remove(field)
decided = []
order = []
for k in sorted(poss, key=lambda k: len(poss[k]), reverse=False):
    order.append(k)
for key in order:
    for fi in decided:
        try:
            poss[key].remove(fi)
        except ValueError:
            pass
    decided.extend(poss[key])
myticketdic = {}
for key in poss:
    myticketdic[poss[key][0]] = myticket[key]
res = 1
for field in rules:
    if field.strip().split(" ")[0] == "departure":
        res = res * myticketdic[field]
print(res)