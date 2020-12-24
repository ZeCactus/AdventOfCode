def compute_slope(x1,y1,x2,y2):
    if x1 == x2:
        return "vertical"
    else:
        return (y2 - y1) / (x2 - x1)
def create_quadrants(x1,y1):
    quadrant = []
    for item in matrix[0:y1+1]:
        quadrant.append(item[0:x1+1])
    quadrants.append(quadrant)
    quadrant = []
    for item in matrix[0:y1+1]:
        quadrant.append(item[x1:len(matrix[0])])
    quadrants.append(quadrant)
    quadrant = []
    for item in matrix[y1:len(matrix)]:
        quadrant.append(item[0:x1+1])
    quadrants.append(quadrant)
    quadrant = []
    for item in matrix[y1:len(matrix)]:
        quadrant.append(item[x1:len(matrix[0])])
    quadrants.append(quadrant)
    return quadrants
def slopes(x, y):
    slope_list = []
    for i in range(0, len(matrix[0])-1):
        slope = compute_slope(x, y, i, 0)
        if slope not in slope_list:
            slope_list.append(slope)
    for i in range(0, len(matrix)):
        slope = compute_slope(x, y, len(matrix[0])-1, i)
        if slope not in slope_list:
            slope_list.append(slope)
    
    for i in range(0, len(matrix[0])):    
        slope = compute_slope(x, y, i, len(matrix)-1)
        if slope not in slope_list:
            slope_list.append(slope)
    for i in range(0, len(matrix)):
        slope = compute_slope(x, y, len(matrix)-1, i)
        if slope not in slope_list:
            print(slope, x, y, len(matrix)-1, i)
            slope_list.append(slope)
    return slope_list
def visible_asteroids(x, y, slope_list):
    viss = 0
    for slope in slope_list:
        if slope == "vertical":
            break
        b = y - slope * x
        for x2 in range(0, x):
            y2 = slope * x + b
            if y2 == int(y2):
                if matrix[int(y2)][x2] == "#":
                    viss += 1
                    break
    return viss
inputf = open("part1.txt", "r")
matrix = [list(line) for line in inputf.read().split()]
inputf.close()
quadrants = []
for y1 in range(0, len(matrix)):
    for x1 in range(0, len(matrix[0])):
        if matrix[y1][x1] == ".":
            continue
        quadrants = create_quadrants(x1,y1)
slope_list = slopes(1,0)
vis = visible_asteroids(1, 0, slope_list)
print(vis)
