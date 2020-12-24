with open("input.txt", "r") as file:
    items = file.readlines()
valid = 0
for item in items:
    pw = item.split(":")[1].strip()
    policy = item.split(":")[0]
    character = policy.split(" ")[1]
    occ = policy.split(" ")[0].split("-")
    poz1 = int(occ[0])
    poz2 = int(occ[1])
    count = 0
    if pw[poz1-1] == character:
        count = count + 1
    if pw[poz2-1] == character:
        count = count + 1
    if count == 1:
        valid = valid + 1
print(valid)
