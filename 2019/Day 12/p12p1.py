inputf = open("input.txt", "r")
values = inputf.read().replace("<","").replace(">","").replace(",","").replace("=","").replace("x","").replace("y","").replace("z","").split("\n")
inputf.close()
planets = []
for planet in values:
    planets.append([int(x) for x in planet.split()])
velocities = [[0,0,0] for i in range(0,4)]
def step():
    global planets, velocities
    for i in range(0, 3):
        for j in range(i+1, 4):
            for k in range(0, 3):
                if planets[i][k] > planets[j][k]:
                    velocities[i][k] -= 1
                    velocities[j][k] += 1
                elif planets[i][k] < planets[j][k]:
                    velocities[i][k] += 1
                    velocities[j][k] -= 1
    for i in range(0, 4):
        for j in range(0, 3):
            planets[i][j] += velocities[i][j]
for i in range(0, 2771):
    step()
##for planet in planets:
##	for i in range(0, 3):
##		planet[i] = abs(planet[i])
##for velocity in velocities:
##	for i in range(0, 3):
##		velocity[i] = abs(velocity[i])
##energy= 0
##for i in range(0, 4):
##    energy += sum(planets[i]) * sum(velocities[i])
##print(energy)
