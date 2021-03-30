x = 0
y = 0
wx = 10
wy = 1
direction = 0
with open("input.txt", "r") as file:
    for line in file:
        command = line[0]
        amount = int(line[1:])
        if command == "L":
            while amount > 0:
                wx, wy = wy, wx
                wx = -wx
                amount = amount - 90
            continue
        if command == "R":
            while amount > 0:
                wx, wy = wy, wx
                wy = -wy
                amount = amount - 90
        if command == "F":
            x = x + (wx * amount)
            y = y + (wy * amount)
            continue
        if command == "E":
            wx = wx + amount
            continue
        if command == "W":
            wx = wx - amount
            continue
        if command == "N":
            wy = wy + amount
            continue
        if command == "S":
            wy = wy - amount
            continue
print(abs(x) + abs(y))