def intcode_computer(program, inputs):
    i = 0
    executed = 0
    while True:
        param_modes = []
        instruction = int(program[i])
        opcode = instruction % 100
        instruction = int(instruction / 100)
        if opcode == 99:
            return True
        elif opcode in [3, 4]:
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
            param = program[i+j]
            if param_modes.pop() == 0:
                param = program[param]
            params.append(param)
        params.reverse()
        if opcode == 1:
            result = params.pop() + params.pop()
            program[program[i+3]] = result
        if opcode == 2:
            result = params.pop() * params.pop()
            program[program[i+3]] = result
        if opcode == 3:
            inp = inputs.pop()
            program[program[i+1]] = inp
        if opcode == 4:
            print(params.pop())
        if opcode == 5:
            if params.pop() != 0:
                i = params.pop()
                continue
        if opcode == 6:
            if params.pop() == 0:
                i = params.pop()
                continue
        if opcode == 7:
            if params.pop() < params.pop():
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
        if opcode == 8:
            if params.pop() == params.pop():
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
        i += param_amount + 1
    return True

inputf = open("input.txt", "r")
program = [int(token) for token in inputf.read().split(",")]
inputs = [int(token) for token in input("Enter inptus: ").split()]intcode_computer(program, inputs)



