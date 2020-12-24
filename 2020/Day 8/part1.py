program = []
def run():
    visited = []
    curr = 0
    acc = 0
    while True:
        if curr == len(program):
            return [0, acc]
        if curr in visited:
            return [-1, acc]
        visited.append(curr)
        instruction = program[curr][0]
        value = int(program[curr][1])
        if instruction == "acc":
            acc = acc + value
            curr = curr + 1
        if instruction == "nop":
            curr = curr + 1
        if instruction == "jmp":
            curr = curr + value

with open("input.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        program.append(line.split())
for i in range(0, len(program)):
    if program[i][0] == "nop":
        program[i][0] = "jmp"
        res = run()
        if res[0] == 0:
            print(res[1])
            break
        else:
            program[i][0] = "nop"
    if program[i][0] == "jmp":
        program[i][0] = "nop"
        res = run()
        if res[0] == 0:
            print(res[1])
            break
        else:
            program[i][0] = "jmp"
    
