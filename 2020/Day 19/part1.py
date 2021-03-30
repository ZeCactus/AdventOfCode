import re
rules = {}
def decompose(rule):
    if len(rule) == 1:
        return rule
    newrule = "("
    for r in rule.split(" "):
        try:
            int(r)
        except ValueError:
            newrule = newrule + r
            continue
        newrule = newrule + decompose(rules[r])
    return newrule.strip() + ")"



regex = ""
strings = []
with open("input.txt", "r") as file:
    for line in file:
        if line == "\n":
            break
        line = line.strip()
        rules[line.split(":")[0]] = line.split(":")[1].strip().replace('"', "")
    for line in file:
        strings.append(line)
regex = decompose(rules["0"]) + "\W"
matches = 0
for string in strings:
    if re.match(regex, string):
        matches = matches + 1
print(matches)
print(regex)