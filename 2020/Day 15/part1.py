numbers = {}
with open("input.txt", "r") as file:
    nrs = file.readline().split(",")
    for i in range(0, len(nrs)):
        numbers[int(nrs[i])] = i+1
prevnr = 0
for turn in range(len(nrs) + 2, 30000001):
    print(turn)
    if prevnr in numbers.keys():
        nr = (turn-1) - numbers[prevnr]
        numbers[prevnr] = turn-1
        prevnr = nr
    else:
        numbers[prevnr] = turn-1
        prevnr = 0
print(nr)