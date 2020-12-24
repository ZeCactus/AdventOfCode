inputf = open("input.txt", "r")
instructions = inputf.read().split("\n")
inputf.close()
keypad = [[1,2,3],[4,5,6],[7,8,9]]
code = []
x = 1
y = 1
for instruction in instructions:
    for ch in instruction:
        if ch == "U":
            if y == 0:
                continue
            else:
                y -= 1
        elif ch == "D":
            if y == 2:
                continue
            else:
                y += 1
        elif ch == "L":
            if x == 0:
                continue
            else:
                x -= 1
        elif ch == "R":
            if x == 2:
                continue
            else:
                x += 1
    code.append(keypad[y][x])
print(code)
