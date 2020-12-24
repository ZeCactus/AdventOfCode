inputf = open("actualsue.txt", "r")
text = inputf.read().split("\n")
inputf.close()
actualsue = {}
for line in text:
    line = line.split()
    actualsue[line[0]] = int(line[1])
inputf = open("input.txt", "r")
suestext = [[x.split() for x in line.split(", ")] for line in inputf.read().split("\n")]
sues = []
for sue in suestext:
    currentsue = {}
    for property in sue:
        currentsue[property[0]] = int(property[1])
    sues.append(currentsue)
nr = 0
for i in range(0, len(sues)):
    thisone = True
    for key in sues[i]:
        if sues[i][key] != actualsue[key]:
            thisone = False
    if thisone == True:
        print(i+1)
