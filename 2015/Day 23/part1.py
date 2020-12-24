values = {"a" : 1, "b" : 0}
inputf = open("input.txt", "r")
instructions = inputf.read().split("\n")
i = 0
while True:
    if i >= len(instructions):
        print(values["b"])
        break
    line = instructions[i]
    instruction = line[0:3]
    if instruction == "inc":
        values[line.split()[1]] += 1
    elif instruction == "tpl":
        values[line.split()[1]] *= 3
    elif instruction == "hlf":
        values[line.split()[1]] = int(values[line.split()[1]]/2)
    elif instruction == "jmp":
        i += int(line.split()[1])
        continue
    elif instruction == "jie":
        if values[line.split()[1].replace(",", "")] % 2 == 0:
            i += int(line.split()[2])
            continue
    elif instruction == "jio":
        if values[line.split()[1].replace(",", "")] == 1:
            i += int(line.split()[2])
            continue
    i += 1
