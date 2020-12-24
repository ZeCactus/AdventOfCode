passports = []
passport = {}
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            passports.append(passport)
            passport = {}
            continue
        data = line.strip().split(" ")
        for item in data:
            passport[item.split(":")[0]] =  item.split(":")[1]
passports.append(passport)
valids = 0
#"byr","iyr","eyr","hgt","hcl","ecl","pid"
fields = ["byr","iyr","eyr", "hgt", "hcl", "ecl", "pid"]
eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for passport in passports:
    valid = True
    for key in fields:
        if key not in passport:
            valid = False
        else:
            if key == "byr" and int(passport["byr"]) not in range(1920, 2003):
                valid = False
            if key == "iyr" and int(passport["iyr"]) not in range(2010, 2021):
                valid = False
            if key == "eyr" and int(passport["eyr"]) not in range(2020, 2031):
                valid = False
            if key == "hgt":
                if passport["hgt"][-2:] == "cm" and int(passport["hgt"][:-2]) not in range(150, 194):
                    valid = False
                if passport["hgt"][-2:] == "in" and int(passport["hgt"][:-2]) not in range(59, 76):
                    valid = False
            if key == "hcl":
                color = passport["hcl"]
                if color[0] != "#":
                    valid = False
                color = color[1:]
                try:
                    x = int(color, 16)
                except ValueError:
                    valid = False
            if key == "ecl" and passport["ecl"] not in eyes:
                valid = False
            if key == "pid":
                if len(passport["pid"]) != 9:
                    valid = False
                else:
                    try:
                        x = int(passport["pid"])
                    except ValueError:
                        valid = False
                
    if valid == True:
        valids = valids + 1
print(valids)
