inputf = open("input.txt", "r")
instructions = inputf.read().split('\n')
d = {}
for instruction in instructions:
    d[instruction.split()[-1]] = None
while instructions:
    for instruction in instructions:
        i = instruction.split()
        if len(i) == 3:
            if i[0].isdigit():
                d[i[2]] = int(i[0])
                instructions.remove(instruction)
                continue
            else:
                if d[i[0]] != None:
                    d[i[2]] = d[i[0]]
                    instructions.remove(instruction)
                    continue
        if len(i) == 4:
            if i[1].isdigit():
                d[i[3]] = ~int(i[1])
                instructions.remove(instruction)
                continue
            else:
                if d[i[1]] != None:
                    d[i[3]] = ~d[i[1]]
                    instructions.remove(instruction)
                    continue
        if len(i) == 5:
            if i[1] == "AND":
                if i[0].isdigit():
                    if i[2].isdigit():
                        d[i[4]] = int(i[0]) & int(i[2])
                        instructions.remove(instruction)
                        continue
                    else:
                        if d[i[2]] != None:
                            d[i[4]] = int(i[0]) & d[i[2]]
                            instructions.remove(instruction)
                            continue
                else:
                    if d[i[0]] != None:
                        if i[2].isdigit():
                            d[i[4]] = d[i[0]] & int(i[2])
                            instructions.remove(instruction)
                            continue
                        else:
                            if d[i[2]] != None:
                                d[i[4]] = d[i[0]] & d[i[2]]
                                instructions.remove(instruction)
                                continue
            if i[1] == "OR":
                if i[0].isdigit():
                    if i[2].isdigit():
                        d[i[4]] = int(i[0]) | int(i[2])
                        instructions.remove(instruction)
                        continue
                    else:
                        if d[i[2]] != None:
                            d[i[4]] = int(i[0]) | d[i[2]]
                            instructions.remove(instruction)
                            continue
                else:
                    if d[i[0]] != None:
                        if i[2].isdigit():
                            d[i[4]] = d[i[0]] | int(i[2])
                            instructions.remove(instruction)
                            continue
                        else:
                            if d[i[2]] != None:
                                d[i[4]] = d[i[0]] | d[i[2]]
                                instructions.remove(instruction)
                                continue
            if i[1] == "LSHIFT":
                if i[0].isdigit():
                    if i[2].isdigit():
                        d[i[4]] = int(i[0]) << int(i[2])
                        instructions.remove(instruction)
                        continue
                    if d[i[2]] != None:
                        d[i[4]] = int(i[0]) << d[i[2]]
                        instructions.remove(instruction)
                        continue
                if d[i[0]] != None:
                    if i[2].isdigit():
                        d[i[4]] = d[i[0]] << int(i[2])
                        instructions.remove(instruction)
                        continue
                    if d[i[2]] != None:
                        d[i[4]] = d[i[0]] << d[i[2]]
                        instructions.remove(instruction)
                        continue
            if i[1] == "RSHIFT":
                if i[0].isdigit():
                    if i[2].isdigit():
                        d[i[4]] = int(i[0]) >> int(i[2])
                        instructions.remove(instruction)
                        continue
                    if d[i[2]] != None:
                        d[i[4]] = int(i[0]) >> d[i[2]]
                        instructions.remove(instruction)
                        continue
                if d[i[0]] != None:
                    if i[2].isdigit():
                        d[i[4]] = d[i[0]] >> int(i[2])
                        instructions.remove(instruction)
                        continue
                    if d[i[2]] != None:
                        d[i[4]] = d[i[0]] >> d[i[2]]
                        instructions.remove(instruction)
                        continue













                
