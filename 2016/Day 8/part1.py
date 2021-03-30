import copy
def rect(display, a, b):
    for i in range(a):
        for j in range(b):
            display[j][i] = "#"
    return display
def row_rotate(display, y, amount):
    row = display[y]
    newrow = copy.copy(row)
    for i in range(50):
        newrow[(i+amount)%50] = row[i]
    display[y] = newrow
    return display
def col_rotate(display, x, amount):
    column = [display[i][x] for i in range(6)]
    newcolumn = copy.copy(column)
    for i in range(6):
        newcolumn[(i+amount)%6] = column[i]
    for i in range(len(newcolumn)):
        display[i][x] = newcolumn[i]
    return display

display = [['.' for x in range(50)] for x in range(6)]

with open("input.txt") as f:
    for line in f:
        if line.split(" ")[0] == "rect":
            parameters = line.split(" ")[1]
            length = int(parameters.split("x")[0])
            width = int(parameters.split("x")[1])
            rect(display, length, width)
        elif line.split(" ")[1] == "row":
            parameters = line.split(" ", 2)[-1]
            x = int(parameters.split(" ")[0].split("=")[1])
            amount = int(parameters.split(" ")[-1])
            display = row_rotate(display, x, amount)
        else:
            parameters = line.split(" ", 2)[-1]
            y = int(parameters.split(" ")[0].split("=")[1])
            amount = int(parameters.split(" ")[-1])
            display = col_rotate(display, y, amount)
pixels = 0
for line in display:
    pixels += line.count("#")
print(pixels)
for line in display:
    print(''.join(line))
