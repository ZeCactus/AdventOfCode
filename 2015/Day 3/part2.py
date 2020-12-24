import operator
inputf = open("input.txt", "r")
dirs = inputf.read()
add = lambda tup1, tup2 : tuple(map(operator.add, tup1, tup2)) 
nr_visited = 1
mov = {'^' : (0, 1), 'v' : (0, -1), ">" : (1, 0), "<" : (-1, 0)}
visited = [(0,0)]
(x, y) = (0, 0)
for char in dirs[::2]:
    (x, y) = add((x, y), mov[char])
    if (x, y) not in visited:
        nr_visited += 1
        visited.append((x, y))
(x, y) = (0, 0)
for char in dirs[1::2]:
    (x, y) = add((x, y), mov[char])
    if (x, y) not in visited:
        nr_visited += 1
        visited.append((x, y))

print(nr_visited)
