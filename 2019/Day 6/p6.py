import copy
class Planet:
    def __init__(self, parent, name):
        self.parent = parent
        self.orbitals = []
        self.name = name
        self.searched = False
    def add_orbital(self, orbital):
        self.orbitals.append(orbital)
def build(orbits):
    planets = {}
    searched = {}
    planets["COM"] = Planet(None, "COM")
    for orbit in orbits:
        parent, child = orbit.split(")")
        if parent not in planets:
            planets[parent] = Planet(None, parent)
        if child not in planets:
            planets[child] = Planet(None, child)
        planets[parent].add_orbital(planets[child])
        planets[child].parent = planets[parent]
    return planets
def count_orbits(planet):
    orbits = 0
    parent = planet.parent
    while parent is not None:
        orbits += 1
        parent = parent.parent
    for x in planet.orbitals:
        orbits += count_orbits(x)
    return orbits


def find_santa(start, santa):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        if path[-1] == santa:
            path.pop(0)
            path.pop()
            return path
        for adjacent in path[-1].orbitals:
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    return False
            



inputf = open("input.txt", "r")
orbits = inputf.read().split()
planets = build(orbits)
you = planets["YOU"]
santa = planets["SAN"]
path = []
result = find_santa(you, santa)
while not result:
    path.append(you.parent)
    you = you.parent
    result = find_santa(you, santa)
path.extend(result)
path.pop(0)
print(len(path))













