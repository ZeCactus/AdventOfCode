harta = []
with open("input.txt", "r") as file:
    for line in file:
        harta.append(line.strip())
total = 1
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for r,d in slopes:
    trees = 0
    posx = 0
    posy = 0
    while posy < len(harta):
        if harta[posy][posx] == "#":
           trees = trees + 1
        posx = posx + r
        posx = posx % len(harta[posy])
        posy = posy + d
    total = total * trees
print(total)
