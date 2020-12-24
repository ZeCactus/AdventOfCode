with open("input.txt", "r") as file:
    items = file.readlines()
valid = 0
for item in items:
    pw = item.split(":")[1].strip()
    policy = item.split(":")[0]
    character = policy.split(" ")[1]
    occ = policy.split(" ")[0].split("-")
    minim = int(occ[0])
    maxim = int(occ[1])
    if pw.count(character)<=maxim and pw.count(character)>=minim:
        valid = valid + 1
print(valid)
