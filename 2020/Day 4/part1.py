passports = []
passport = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            passports.append(passport)
            passport = []
            continue
        data = line.strip().split(" ")
        for item in data:
            passport.append(item.split(":")[0])
valids = 0
for passport in passports:
    if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport):
        valids = valids + 1
print(valids)
