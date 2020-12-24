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
            address = i+j
            mode = param_modes.pop()
            if mode == 0:
                address = program[address]
            params.append(address)
        params.reverse()
        if opcode == 1:
            result = program[params.pop()] + program[params.pop()]
            program[params.pop()] = result
        if opcode == 2:
            result = program[params.pop()] * program[params.pop()]
            program[params.pop()] = result
        if opcode == 3:
            inp = inputs.pop()
            program[params.pop()] = inp
        if opcode == 4:
            print(program[params.pop()])
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
        i += param_amount + 1
    return True
