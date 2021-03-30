mems = {}
mask = "X" * 36
with open("test.txt", "r") as file:
    for line in file:
        if line[0:3] == "mem":
            address = int(line.split("[")[1].split("]")[0])
            value = int(line.split("=")[1])
            value = f'{value:036b}'
            newval = ""
            for i in range(0, 36):
                if mask[i] == "X":
                    newval = newval + value[i]
                else:
                    newval = newval + mask[i]
            mems[address] = int(newval, 2)

        if line[0:4] == "mask":
            mask = line.split("=")[1].strip()
total = 0
for nr in mems:
    total = total + mems[nr]
print(total)