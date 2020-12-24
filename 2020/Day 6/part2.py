groups = []
group = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            groups.append(group)
            group = []
            continue
        group.append(line)
    groups.append(group)
questions = 0
for group in groups:
    people = len(group)
    control = {}
    for person in group:
        for char in person:
            if char in control:
                control[char] = control[char] + 1
            else:
                control[char] = 1
    for key in control:
        if control[key] == people:
            questions = questions + 1
print(questions)
