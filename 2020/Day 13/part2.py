import math
busses = []
numbers = []
with open("input.txt", "r") as file:
    time = int(file.readline())
    for val in file.readline().strip().split(","):
        if val == "x":
            busses.append(val)
            continue
        busses.append(int(val))
        numbers.append(int(val))
busses.append(0)
total = 0
jump = busses[0]
while len(busses) - busses.count("x") > 2:
    for i in range(1, len(busses)):
        if busses[i] != "x":
            break
    total = total + i
    first = busses[0]
    second = busses[i]
    cycle = first
    while True:
        cycle = cycle + jump
        if (cycle + total) % second == 0:
            break
    busses = busses[i+1:]
    jump = jump * second
    busses.insert(0, cycle)
print(busses[0])




