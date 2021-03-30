import copy
mems = {}
mask = "X" * 36
with open("input.txt", "r") as file:
    for line in file:
        if line[0:3] == "mem":
            address = int(line.split("[")[1].split("]")[0])
            value = int(line.split("=")[1])
            address = f'{address:036b}'
            newaddress = ""
            for i in range(0, 36):
                if mask[i] == "X":
                    newaddress = newaddress + mask[i]
                elif mask[i] == "0":
                    newaddress = newaddress + address[i]
                elif mask[i] == "1":
                    newaddress = newaddress + "1"
            addresses = [""]
            for i in range(0, 36):
                newaddresses = []
                newadd = ""
                for add in addresses:
                    if newaddress[i] == "X":
                        newadd = add + "1"
                        newaddresses.append(newadd)
                        newadd = add + "0"
                        newaddresses.append(newadd)
                    else:
                        newadd = add + newaddress[i]
                        newaddresses.append(newadd)
                addresses = copy.copy(newaddresses)
            for abc in addresses:
                intadd = int(abc, 2)
                mems[intadd] = value
        if line[0:4] == "mask":
            mask = line.split("=")[1].strip()
total = 0
for nr in mems:
    total = total + mems[nr]
print(total)
#3638094973423
#3638094973423