bags = {}
with open("input.txt", "r") as file:
    for rule in file:
        rule = rule.strip()
        rule = rule.split("bags contain")
        rule[1] = rule[1].split(',')
        temp = {}
        if rule[1][0] == " no other bags.":
            temp = {}
        else:
            temp = {}
            for r in rule[1]:
                r = r.strip()
                r.replace(".", "")
                r = r.replace("bags.", "bags")
                r = r.replace("bags", "bag")
                r = r.replace(" bag", "")
                r = r.split(" ", 1)
                temp[r[1].strip().replace(".", "")] = r[0]
        bags[rule[0].strip()] = temp
targets = [["shiny gold", 1]]
total = 0

while targets:
    new = []
    for target in targets:
        total = total + int(target[1])
        for bag in bags[target[0]]:
            new.append([bag, int(bags[target[0]][bag]) * target[1]])
    targets = new
print(total - 1)
