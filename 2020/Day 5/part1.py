seats = []
with open("input.txt", "r") as file:
    for line in file:
        seats.append(line.strip())
maxid = 0
for seat in seats:
    min = 0
    max = 127 
    for i in range(0, 7):
        if seat[i] == "F":
            max = (max-min)//2+min
        if seat[i] == "B":
            min = max - (max - min)//2
    row = min
    min = 0
    max = 7
    for i in range(7, 10):
        if seat[i] == "L":
            max = (max-min)//2+min
        if seat[i] == "R":
            min = max - (max - min)//2
    col = min
    id = row * 8 + col
    if id > maxid:
        maxid = id
print(maxid)
