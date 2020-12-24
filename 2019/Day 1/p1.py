input = open("input.txt")
fuel = 0
for line in input:
    mass = int(line)
    while mass // 3 - 2 > 0:
        fuel = fuel + mass//3 - 2
        mass = mass // 3 - 2
print(fuel)
