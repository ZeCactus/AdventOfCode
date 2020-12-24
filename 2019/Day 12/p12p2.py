import copy
inputf = open("input.txt", "r")
values = inputf.read().replace("<","").replace(">","").replace(",","").replace("=","").replace("x","").replace("y","").replace("z","").split("\n")
inputf.close()
planets = []
for planet in values:
    planets.append([int(x) for x in planet.split()])
velocities = [[0,0,0] for i in range(0,4)]
def step(k):
    global planets, velocities
    for i in range(0, 3):
        for j in range(i+1, 4):
            if planets[i][k] > planets[j][k]:
                velocities[i][k] -= 1
                velocities[j][k] += 1
            elif planets[i][k] < planets[j][k]:
                velocities[i][k] += 1
                velocities[j][k] -= 1
    for i in range(0, 4):
            planets[i][k] += velocities[i][k]
original = copy.deepcopy(planets)
taken = 0
states = [copy.deepcopy(planets + velocities)]
while True:
    step(0)
    taken += 1
    if planets+velocities in states:
        break
    states.append(copy.deepcopy(planets))

