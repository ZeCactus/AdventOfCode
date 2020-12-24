import copy
from PIL import Image
img = Image.new("RGB", (250,250), color = "black")
pixels = img.load()
hull = [[0 for i in range(0, 250)] for i in range(0, 250)]
x = 125
y = 125
hull = copy.deepcopy(hull)
direction = 0
painted = copy.deepcopy(hull)
hull[x][y] = 1
def intcode_computer(program):
    global hull, orientation,x,y,direction
    control = 1
    i = 0
    offset = 0
    while True:
        param_modes = []
        instruction = int(program[i])
        opcode = instruction % 100
        instruction = int(instruction / 100)
        if opcode == 99:
            return True
        elif opcode in [3, 4, 9]:
            param_amount = 1
        elif opcode in [5, 6]:
            param_amount = 2
        elif opcode in [1, 2, 7, 8]:
            param_amount = 3
        for j in range(0,param_amount):
            param_modes.append(instruction % 10)
            instruction = int(instruction / 10)
        param_modes.reverse()
        params = []
        for j in range(1, param_amount+1):
            address = i+j
            mode = param_modes.pop()
            if mode == 0:
                address = program[address]
            if mode == 2:
                address = program[address] + offset
            if address > len(program) - 1:
                program.extend([0] * (address - len(program) + 1))
            params.append(address)
        params.reverse()
        if opcode == 1:
            result = program[params.pop()] + program[params.pop()]
            program[params.pop()] = result
        if opcode == 2:
            result = program[params.pop()] * program[params.pop()]
            program[params.pop()] = result
        if opcode == 3:
            inp = hull[x][y]
            program[params.pop()] = inp
        if opcode == 4:
            output = program[params.pop()]
            if control == 1:
                hull[x][y] = output
                painted[x][y] += 1
            if control == -1:
                if output == 0:
                    direction -= 1
                if output == 1:
                    direction += 1
                direction %= 4
                if direction % 2 == 0:
                    y += ((direction - 1) )
                else:
                    x += ((direction - 2) )
                    
            control *= -1
        if opcode == 5:
            if program[params.pop()] != 0:
                i = program[params.pop()]
                continue
        if opcode == 6:
            if program[params.pop()] == 0:
                i = program[params.pop()]
                continue
        if opcode == 7:
            if program[params.pop()] < program[params.pop()]:
                program[params.pop()] = 1
            else:
                program[params.pop()] = 0
        if opcode == 8:
            if program[params.pop()] == program[params.pop()]:
                program[params.pop()] = 1
            else:
                program[params.pop()] = 0
        if opcode == 9:
            offset += program[params.pop()]
        i += param_amount + 1
    return True


inputf = open("input.txt", "r")
program = [int(token) for token in inputf.read().split(",")]
intcode_computer(program)
