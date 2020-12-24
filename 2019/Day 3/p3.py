import copy
import math
import time
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def __str__(self):
        return str(self.x) + ", " + str(self.y)
        
class Line:
    def __init__(self):
        self.start = Point()
        self.end = Point()
        self.steps = 0
    def __str__(self):
        return str(self.start) + ", " + str(self.end)
        

def orientation(p1, p2, p3):
    value = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)
    if value == 0:
        return 0
    elif value > 0:
        return 1
    else:
        return 2

def onsegment(p1, p2, p3):
    if p2.x <= max(p1.x, p3.x) and p2.x >= min(p1.x, p3.x) and \
       p2.y <= max(p1.y, p3.y) and p2.y >= min(p1.y, p3.y):
        return True
    return False

def intersect(line1, line2):
    o1 = orientation(line1.start, line1.end, line2.start)
    o2 = orientation(line1.start, line1.end, line2.end)
    o3 = orientation(line2.start, line2.end, line1.start)
    o4 = orientation(line2.start, line2.end, line1.end)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and onsegment(line1.start, line2.start, line1.end):
        return True
    if o2 == 0 and onsegment(line1.start, line2.end, line1.end):
        return True
    if o3 == 0 and onsegment(line2.start, line1.start, line2.end):
        return True
    if o3 == 0 and onsegment(line2.start, line1.end, line2.end):
        return True
    return False
    
    
def intersection(line1, line2):
    a1 = line1.end.y - line1.start.y
    b1 = line1.start.x - line1.end.x
    c1 = a1 * line1.start.x + b1 * line1.start.y

    a2 = line2.end.y - line2.start.y
    b2 = line2.start.x - line2.end.x
    c2 = a2 * line2.start.x + b2 * line2.start.y

    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return False
    else:
        x = (b2 * c1 - b1 * c2)/determinant
        y = (a1 * c2 - a2 * c1)/determinant
        intersect = Point()
        intersect.x = x
        intersect.y = y
        return intersect
def compute_distance(point):
    return abs(point.x) + abs(point.y)

start = time.time()
file = open("input.txt","r")
wire1 = file.readline().split(",")
wire1_path = []
pos = Point()
pos.x = 0
pos.y = 0
steps = 0
for x in wire1:
    line = Line()
    line.start.x = pos.x
    line.start.y = pos.y
    direction = x[0]
    move = int(x[1:])
    if direction == "U":
        pos.y = pos.y + move
    elif direction == "D":
        pos.y = pos.y - move
    elif direction == "L":
        pos.x = pos.x - move
    elif direction == "R":
        pos.x = pos.x + move
    line.end.x = pos.x
    line.end.y = pos.y
    steps = steps + int(x[1:])
    line.steps = steps
    wire1_path.append(copy.deepcopy(line))

wire2 = file.readline().split(",")
pos.x = 0
pos.y = 0
steps = 0
nearest_dist = float("inf")
nearest = Point()
for x in wire2:
    line = Line()
    line.start.x = pos.x
    line.start.y = pos.y
    direction = x[0]
    move = int(x[1:])
    if direction == "U":
        pos.y = pos.y + move
    elif direction == "D":
        pos.y = pos.y - move
    elif direction == "L":
        pos.x = pos.x - move
    elif direction == "R":
        pos.x = pos.x + move
    line.end.x = pos.x
    line.end.y = pos.y
    steps = steps + int(x[1:])
    line.steps = steps
    workline = copy.deepcopy(line)
    for k in wire1_path:
        stepcopy = steps + k.steps
        if intersect(workline, k):
            if intersection(workline, k) != False:
                intersection_point = intersection(workline, k)
                if workline.start.x == workline.end.x:
                    stepcopy -= abs(workline.end.y - intersection_point.y)
                if workline.start.y == workline.end.y:
                    stepcopy -= abs(workline.end.x - intersection_point.x)
                if k.start.x == k.end.x:
                    stepcopy -= abs(k.end.y - intersection_point.y)
                if k.start.y == k.end.y:
                    stepcopy -= abs(k.end.x - intersection_point.x)
                if stepcopy < nearest_dist and intersection_point.x != 0 and intersection_point.y != 0:
                    nearest = copy.deepcopy(intersection_point)
                    nearest_dist = stepcopy
print(str(nearest_dist))
print("Time: " + str((time.time() - start) * 100) + "ms")











    
