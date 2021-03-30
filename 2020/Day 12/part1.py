x = 0
y = 0
direction = 0
with open("input.txt", "r") as file:
    for line in file:
        command = line[0]
        amount = int(line[1:])
        if command == "L":
            direction = direction - amount
            direction = direction%360
            continue
        if command == "R":
            direction = direction + amount
            direction = direction % 360
            continue
        if command == "F":
            if direction == 0:
                x = x + amount
                continue
            if direction == 90:
                y = y - amount
                continue
            if direction == 180:
                x = x - amount
                continue
            if direction == 270:
                y = y + amount
                continue
        if command == "E":
            x = x + amount
            continue
        if command == "W":
            x = x - amount
            continue
        if command == "N":
            y = y + amount
            continue
        if command == "S":
            y = y - amount
            continue
print(abs(x) + abs(y))