seats = []
with open("input.txt", "r") as file:
    for line in file:
        seats.append(line.strip())
ids = []
for i in range(10, 126):
    for j in range(0, 8):
        ids.append(i*8+j)
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
    ids.pop(ids.index(id))
print(ids)
