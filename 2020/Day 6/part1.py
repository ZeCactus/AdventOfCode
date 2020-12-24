groups = []
group = ""
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            groups.append(group)
            group = ""
            continue
        group = group + line
    groups.append(group)
questions = 0
for group in groups:
    control = []
    for char in group:
        if char not in control:
            control.append(char)
            questions = questions + 1
print(questions)
