inputf = open("input.txt", "r")
nice = 0
for line in inputf.read().split():
    naughty = True
    for i in range(0, len(line)-2):
        if line[i] == line[i+2]:
            naughty = False
            break
    if naughty == True:
        continue
    naughty = True
    for i in range(0, len(line)-1):
        if line.count(line[i] + line[i+1]) > 1:
            naughty = False
            break
    if naughty == True:
        continue
    nice += 1
print(nice)
