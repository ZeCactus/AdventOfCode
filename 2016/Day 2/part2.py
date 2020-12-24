inputf = open("input.txt", "r")
instructions = inputf.read().split("\n")
inputf.close()
keypad = [[0,0,1,0,0], [0,2,3,4,0], [5,6,7,8,9], [0,"A","B","C",0], [0,0,"D",0,0]]
x = 0
y = 2
code = []
for instruction in instructions:
    for ch in instruction:
        if ch == "U":
            y -= 1
            if y < 0 or keypad[y][x] == 0:
                y += 1
        elif ch == "D":
            y += 1
            if y > 4 or keypad[y][x] == 0:
                y -= 1
        elif ch == "L":
            x -= 1
            if x < 0 or keypad[y][x] == 0:
                x += 1
        elif ch == "R":
            x += 1
            if x > 4 or keypad[y][x] == 0:
                x -= 1
    code.append(keypad[y][x])
print(code)
